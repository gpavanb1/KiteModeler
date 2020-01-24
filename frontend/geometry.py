from .helper import slider_and_label
import dash_html_components as html


slider_h1 = slider_and_label('h1', 2.0, 40, 0.5, 'Top to Frame Intersection (H1 - cm)', 12.7)
slider_h2 = slider_and_label('h2', 2.0, 40, 0.5, 'Frame Intersection to Bottom (H2 - cm)', 25.4)
slider_w1 = slider_and_label('w1', 2.0, 40, 0.5, 'Side-to-Side (W1 - cm)', 25.4)
slider_t = slider_and_label('t', 2.0, 40, 0.5, 'Tail Length (T - cm)', 0.0)

geometry_components = html.Div([
    html.Br(),
    slider_h1,
    slider_h2,
    slider_w1,
    slider_t
])