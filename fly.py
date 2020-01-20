from environment_dicts import Environments


class FlyParameters:
    def __init__(self, wind_speed, altitude, line, env):
        self.wind_speed = wind_speed
        self.altitude = altitude
        self.line = line
        # TODO : Payload
        self.env = Environments[env]
