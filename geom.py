class DiamondGeometry:
    def __init__(self, h1, h2, w1):
        self.h1 = h1
        self.h2 = h2
        self.w1 = w1

    def surface_area(self):
        return 0.5*(self.h1 + self.h2)*self.w1

    def frame(self):
        return self.h1 + self.h2 + self.w1



