import math

# https://www.grc.nasa.gov/WWW/k-12/VirtualAero/BottleRocket/airplane/kitebrid.html


def knot_angle(b, k, h):
    ret = (k*k + h*h - (b - k)*(b - k))/(2*k*h)
    if abs(ret) > 1:
        return 0.0
    else:
        return math.acos(ret)


class BridleGeometry:
    def __init__(self, b, k, h):
        try:
            # TODO : Raise error if negative b, k, h
            if b <= k:
                raise ValueError("Knot must be larger than bridle")
            self.B = b
            self.K = k
            self.H = h
            self.A = knot_angle(b, k, h)
            self.Xb = k*math.sin(self.A)
            self.Yb = k*math.cos(self.A)

        except ValueError as e:
            print(e)
