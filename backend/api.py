from .geom import DiamondGeometry
from .bridle import BridleGeometry
from .fly import FlyParameters
from .composition import Composition
from .dashboard import Dashboard
from .helper import dotdict


def solve(inp):
    inp = dotdict(inp)
    geom = DiamondGeometry(inp.h1, inp.h2, inp.w1, inp.t)
    bridle = BridleGeometry(inp.B, inp.K, geom.h())
    fly = FlyParameters(inp.wind_speed, inp.altitude,
                        inp.line_length, inp.env_name)
    compo = Composition(inp.surface,
                        inp.frame,
                        inp.tail,
                        inp.line)
    dashboard = Dashboard(geom, bridle, fly, compo)
    ret_dict = dashboard.__dict__

    # Remove objects from dictionary
    toDelete = ["geom", "bridle", "fly", "compo", "min_func"]
    for i in toDelete:
        ret_dict.pop(i)
    return ret_dict

# Thanks to OSI Digital
