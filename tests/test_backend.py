from backend.api import solve
from backend.helper import  dotdict


inp = {
    'h1': 12.7,
    'h2': 25.4,
    'w1': 25.4,
    'B': 39.37,
    'K': 30.48,
    'wind_speed': 3.048,
    'altitude': 0.0,
    'line_length': 30.48,
    'env_name': "Earth",
    'surface': "Plastic",
    'frame': "1/4 Balsa",
    'tail': "1 in Plastic",
    'line': "Nylon"
}

inp = dotdict(inp)
print(solve(inp))
