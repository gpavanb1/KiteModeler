import dash_html_components as html
import dash_bootstrap_components as dbc


def create(inp):
    res = {k: str(round(v, 3)) for k, v in inp.items()}
    body = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Lift (gm)" + " " + res['_lift']),
                            html.H4("Drag (gm)" + " " + res['_drag']),
                            html.H4("Weight (gm)" + " " + res['_weight']),
                            html.H4("Tension (gm)" + " " + res['_tension']),
                            html.H4("Angle of attack (deg)" + " " + res['_aoa_no_torque_degrees']),
                            html.H4("Pressure (kPa)" + " " + res['pressure'])
                        ],
                        className='md-5',
                    ),
                    dbc.Col(
                        [
                            html.Img(id='image', src="", width="300px", height="300px")
                        ]
                    ),
                    dbc.Col(
                        [
                            html.H4("Surface Area (cm2)" + " " + res['_surface_area']),
                            html.H4("cp (cm)" + " " + res['_cp']),
                            html.H4("cg (cm)" + " " + res['_cg']),
                            html.H4("Range (m)" + " " + res['_range']),
                            html.H4("Height (m)" + " " + res['_height']),
                            html.H4("Temperature (K)" + " " + res['temperature'])
                        ],
                        className='md-5'
                    )
                ]
            )
        ]
    )
    return body
