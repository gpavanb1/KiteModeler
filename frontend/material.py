from .helper import dropdown_and_label
import dash_html_components as html

options_surface = [
    {'label': "Plastic", 'value': "Plastic"},
    {'label': "Tissue Paper", 'value': "Tissue Paper"},
    {'label': "Rip Stop", 'value': "Rip Stop"},
    {'label': "Silk Span", 'value': "Silk Span"},
    {'label': "Cellophane", 'value': "Cellophane"}
]

options_frame = [
    {'label': "1/4 Balsa", 'value': "1/4 Balsa"},
    {'label': "1/8 Balsa", 'value': "1/8 Balsa"},
    {'label': "1/4 Birch", 'value': "1/4 Birch"},
    {'label': "3/8 Plastic Tube", 'value': "3/8 Plastic Tube"},
    {'label': "Skewer Stick", 'value': "Skewer Stick"}
]

options_tail = [
    {'label': "1 in Plastic", 'value': "1 in Plastic"},
    {'label': "3 in Plastic", 'value': "3 in Plastic"},
    {'label': "1 in Nylon", 'value': "1 in Nylon"}
]

options_line = [
    {'label': "Nylon", 'value': "Nylon"},
    {'label': "Cotton", 'value': "Cotton"}
]


dropdown_surface = dropdown_and_label('surface', options_surface, 'Plastic', 'Surface')
dropdown_frame = dropdown_and_label('frame', options_frame, '1/4 Balsa', 'Frame')
dropdown_tail = dropdown_and_label('tail', options_tail, '1 in Plastic', 'Tail')
dropdown_line = dropdown_and_label('line', options_line, 'Nylon', 'Line')

material_components = html.Div([
    html.Br(),
    dropdown_surface,
    dropdown_frame,
    dropdown_tail,
    dropdown_line
])