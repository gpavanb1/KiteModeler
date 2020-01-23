import dash_core_components as dcc
import dash_html_components as html


def slider_and_label(_id, _min, _max, _step, label):
    return html.Div([
        html.H4(label + ":"),
        dcc.Slider(
            id=_id,
            className='slider',
            min=_min,
            max=_max,
            step=_step,
            tooltip={'always_visible': True},
            value=0.5*(_min + _max))
    ])