from geom import DiamondGeometry
from bridle import BridleGeometry
from fly import FlyParameters
from composition import Composition
from dashboard import Dashboard

geom = DiamondGeometry(12.7, 25.4, 25.4)
bridle = BridleGeometry(39.37, 30.48, geom.h())
fly = FlyParameters(3.048, 0.0, 30.48, "Earth")
compo = Composition("Plastic", "1/4 Balsa", "1 in Plastic", "Nylon")
dashboard = Dashboard(geom, bridle, fly, compo)
print(dashboard.__dict__)
