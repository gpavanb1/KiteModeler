import math

# https://www.grc.nasa.gov/WWW/k-12/VirtualAero/BottleRocket/airplane/kitebrid.html


def knot_angle(b, k, h):
    return math.acos((k*k + h*h - (b - k)*(b - k))/(2*k*h))


class BridleGeometry:
    def __init__(self, b, k, t, h):
        try:
            # TODO : Raise error if negative b, k, t, h
            if b > k:
                raise ValueError("Bridle is greater than Knot")
            self.B = b
            self.K = k
            self.T = t
            self.H = h
            self.A = knot_angle(b, k, h)
            self.Xb = k*math.cos(self.A)
            self.Yb = k*math.sin(self.A)

        except ValueError as e:
            print(e.error)
