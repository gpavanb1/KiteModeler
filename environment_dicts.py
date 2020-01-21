from environment import Environment
import math


# Source for Earth
# https://www.grc.nasa.gov/WWW/K-12/airplane/atmosmet.html
def earth_pressure(h):
    return 101.29 * pow(earth_temperature(h) / 288.08, 5.256)


def earth_temperature(h):
    return 273.1 + 15.04 - 0.00649 * h


Environments = {
    "Earth": Environment(earth_pressure, earth_temperature),
    # TODO : Add Mars
}
