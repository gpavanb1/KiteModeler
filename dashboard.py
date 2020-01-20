class Dashboard:
    def __init__(self, geom, bridle, fly, compo):
        self.geom = geom
        self.bridle = bridle
        self.fly = fly
        self.compo = compo

        self._lift = lift(geom, bridle, fly)
        self._drag = drag(geom, bridle, fly)
        self._weight = kite_weight(geom, compo)
        self._tension = tension()
        self._cg =
        self._cp =
        self._surface_area = geom.surface_area()
        self._frame = geom.frame()
        self._torque =
        # AoA - angle of attack
        # Solve such that torque is zero
        self._aoa =
        self._range =
        self._height =
        # Get sea level properties
        self.pressure = fly.env.pressure(0)
        self.temperature = fly.env.temperature(0)

    def lift(self, geom, bridle, fly):
        pass

    def drag(self, geom, bridle, fly):
        pass

    def kite_weight(geom, compo):
        pass

