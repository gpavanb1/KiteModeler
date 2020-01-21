import math
from scipy.optimize import fsolve


class Dashboard:
    def __init__(self, geom, bridle, fly, compo):
        self.geom = geom
        self.bridle = bridle
        self.fly = fly
        self.compo = compo

        # Weight
        self._weight = self.kite_weight()

        # Center of pressure and gravity
        self._cg = self.cg()
        self._cp = self.geom.cp()

        # Geometric parameters
        self._surface_area = self.geom.surface_area()
        self._frame = self.geom.frame()

        # Solve such that torque is zero
        self._aoa_no_torque = fsolve(self.torque, 0.0)[0]
        self._aoa_no_torque_degrees = self._aoa_no_torque * 180 / math.pi

        # Calculate corresponding lift and drag
        self._lift = self.lift(self._aoa_no_torque)
        self._drag = self.drag(self._aoa_no_torque)

        # Source : https://www.grc.nasa.gov/WWW/K-12/airplane/kitefor.html
        self._horiz_tension = self._drag
        self._vert_tension = self._lift - self._weight
        self._tension = math.sqrt(pow(self._horiz_tension, 2) + pow(self._vert_tension, 2))

        # Height and range
        self._range = self.range()
        self._height = self.height()

        # Get sea level properties
        self.pressure = fly.env.pressure(0)
        self.temperature = fly.env.temperature(0)

    def lift(self, a):
        cl = self.geom.cl(a)
        rho = self.compo.surface.density
        A = self.geom.surface_area()
        V = self.fly.wind_speed
        return cl * A * rho * V * V / 2

    def drag(self, a):
        cd = self.geom.cd(a)
        rho = self.compo.surface.density
        A = self.geom.surface_area()
        V = self.fly.wind_speed
        return cd * A * rho * V * V / 2

    def kite_weight(self):
        w_surf = self.compo.surface.density * self.geom.surface_area()
        w_frameH = self.compo.frame.density * self.geom.w1
        w_frameV = self.compo.frame.density * (self.geom.h1 + self.geom.h2)
        w_tail = self.compo.tail.density * self.geom.t
        return w_frameH + w_frameV + w_surf + w_tail

    def torque(self, a):
        L = self.lift(a)
        D = self.drag(a)
        W = self._weight
        cp = self._cp
        cg = self._cg
        xb = self.bridle.Xb
        yb = self.bridle.Yb

        T = - L * math.cos(a) * (yb - cp) \
            - L * math.sin(a) * xb \
            + D * math.cos(a) * xb \
            - D * math.sin(a) * (yb - cp) \
            + W * math.cos(a) * (yb - cg) \
            + W * math.sin(a) * xb

        return T

    def catenary_equation(self, x):
        # Unit line weight
        p = self.compo.line.density
        # Line length
        s = self.fly.line
        g = s * p
        L = self._lift
        D = self._drag
        W = self._weight

        # Kite won't fly
        if L < g + W:
            return 0.0

        # Integration constants
        c1 = math.asin((L - g - W) / D)
        c2 = -(D / p) * math.cosh(c1)

        # Source: https://www.grc.nasa.gov/WWW/K-12/airplane/kitesag.html
        return c2 + (D / p) * math.cosh(p * x / D + c1)

    def range(self):
        # Unit line weight
        p = self.compo.line.density
        # Line length
        s = self.fly.line
        g = s * p
        L = self._lift
        D = self._drag
        W = self._weight

        # Kite won't fly
        if L < g + W:
            return 0.0

        # Source: https://www.grc.nasa.gov/WWW/K-12/airplane/kitesag.html
        return (D / p) * (math.asinh((L - W) / D) - math.asinh((L - g - W) / D))

    def height(self):
        return self.catenary_equation(self.range())

    def cg(self):
        w_surf = self.compo.surface.density * self.geom.surface_area()
        h_surf = (self.geom.h1 + self.geom.h2) / 2
        w_frameH = self.compo.frame.density * self.geom.w1
        h_frameH = self.geom.h2
        w_frameV = self.compo.frame.density * (self.geom.h1 + self.geom.h2)
        h_frameV = (self.geom.h1 + self.geom.h2) / 2
        w_tail = self.compo.tail.density * self.geom.t
        h_tail = - self.geom.t / 2
        dot_prod = w_surf * h_surf + w_frameH * h_frameH + \
                   w_frameV * h_frameV + w_tail * h_tail
        return dot_prod / self._weight

