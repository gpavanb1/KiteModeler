class Environment:
    def __init__(self, pressure, temperature):
        self.pressure = pressure
        self.temperature = temperature

    def density(self, h):
        # Ideal gas law
        p = 1.e3 * self.pressure(h)
        T = self.temperature(h)
        R = 8.314
        M = 28.97e-3
        return (p * M) / (R * T)
