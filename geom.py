import math


class DiamondGeometry:
    def __init__(self, h1, h2, w1, t=0):
        self.h1 = h1
        self.h2 = h2
        self.w1 = w1
        self.AR = self.aspect_ratio()
        # Tail length
        self.t = t

    def h(self):
        return self.h1 + self.h2

    def surface_area(self):
        return 0.5 * (self.h1 + self.h2) * self.w1

    def frame(self):
        return self.h1 + self.h2 + self.w1

    def aspect_ratio(self):
        s = self.w1
        A = self.surface_area()
        return s * s / A

    # Source: https://www.grc.nasa.gov/WWW/K-12/airplane/kitelift.html
    def cl(self, a):
        Clo = 2 * math.pi * a
        return Clo / (1 + Clo / (math.pi * self.AR))

    # Source: https://www.grc.nasa.gov/WWW/K-12/airplane/kitedrag.html
    def cd(self, a):
        Cdo = 1.28 * math.sin(a)
        return Cdo + pow(self.cl(a), 2) / (.7 * math.pi * self.AR)

    # Area-weighted average of triangle centroids
    def cp(self):
        return 0.5 * (self.h1 + self.h2) + self.h2 / 3

