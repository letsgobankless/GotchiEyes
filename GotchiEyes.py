import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import flask

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    # Row for content
        # Column for inputs
        html.Div([
            html.H1("Aavegotchi Shape and Color Selector"),
            html.H3("EYS Slider"),
            dcc.Slider(
                id='EYS-slider',
                min=0,
                max=99,
                value=0,
                marks={i: str(i) for i in [0, 1, 2, 5, 7, 10, 15, 20, 25, 42, 58, 75, 80, 85, 90, 93, 95, 97, 98]},
                step=1
            ),
            html.H3("EYC Slider"),
            dcc.Slider(
                id='EYC-slider',
                min=0,
                max=99,
                value=0,
                marks={i: str(i) for i in [0, 1, 2, 5, 7, 10, 15, 20, 25, 42, 58, 75, 80, 85, 90, 93, 95, 97, 98]},
                step=1
            ),
            html.H3("Collateral Dropdown"),
            dcc.Dropdown(
                id='collateral-dropdown',
                options=[
                    {'label': i, 'value': i} for i in ['maAAVE', 'amAAVE', 'maDAI', 'amDAI',
                                                       'maWETH', 'maLINK', 'maUSDC', 'amUSDC',
                                                       'maYFI', 'maUNI', 'maTUSD', 'maUSDT',
                                                       'amUSDT', 'amWMATIC', 'amWBTC', 'amWETH']
                ],
                value='maAAVE'
            ),
            html.H3("Select Haunt"),
            dcc.RadioItems(
                id='haunt-toggle',
                options=[
                    {'label': 'Haunt 1', 'value': 'Haunt1'},
                    {'label': 'Haunt 2', 'value': 'Haunt2'}
                ],
                value='Haunt1',
                labelStyle={'display': 'inline-block'}
            ),
        ], style={'width': '50%', 'display': 'inline-block'}),

        # Column for outputs
        html.Div([
            html.H1("Output Image"),
            html.Div([
                html.H3("Eyes Shape"),
                html.Img(id='shape-image', style={'max-width': '100%', 'max-height': '400px', 'position': 'relative'}),
                html.H3("Eyes Color"),
                html.Div(id='color-overlay', style={'position': 'absolute', 'width': '100%', 'height': '100%'})
        ], style={'position': 'relative'}),
    ], style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top'})
])

# Define callback to update image and color
@app.callback(
    Output('shape-image', 'src'),
    Output('color-overlay', 'style'),
    Input('EYS-slider', 'value'),
    Input('EYC-slider', 'value'),
    Input('collateral-dropdown', 'value'),
    Input('haunt-toggle', 'value')
)
def update_output(EYS, EYC, collateral, haunt):
    # Determine shape based on EYS and collateral
    if EYS == 0:
        shape = 'mythical-low-1.svg' if haunt == 'Haunt1' else 'Aavegotchi-H2-EyesShape-Mythical-Low-1.svg'
    elif EYS == 1:
        shape = 'mythical-low-2.svg' if haunt == 'Haunt1' else 'Aavegotchi-H2-EyesShape-Mythical-Low-2.svg'
    elif 2 <= EYS <= 4:
        shape = 'rare-low-1.svg'
    elif 5 <= EYS <= 6:
        shape = 'rare-low-2.svg'
    elif 7 <= EYS <= 9:
        shape = 'rare-low-3.svg'
    elif 10 <= EYS <= 14:
        shape = 'uncommon-low-1.svg'
    elif 15 <= EYS <= 19:
        shape = 'uncommon-low-2.svg'
    elif 20 <= EYS <= 24:
        shape = 'uncommon-low-3.svg'
    elif 25 <= EYS <= 41:
        shape = 'common-1.svg'
    elif 42 <= EYS <= 57:
        shape = 'common-2.svg'
    elif 58 <= EYS <= 74:
        shape = 'common-3.svg'
    elif 75 <= EYS <= 79:
        shape = 'uncommon-high-1.svg'
    elif 80 <= EYS <= 84:
        shape = 'uncommon-high-2.svg'
    elif 85 <= EYS <= 89:
        shape = 'uncommon-high-3.svg'
    elif 90 <= EYS <= 92:
        shape = 'rare-high-1.svg'
    elif 93 <= EYS <= 94:
        shape = 'rare-high-2.svg'
    elif 95 <= EYS <= 97:
        shape = 'rare-high-3.svg'
    elif EYS > 97:
        if collateral in ['maAAVE', 'amAAVE']:
            shape = 'AAVE-collateral.svg'
        elif collateral in ['maDAI', 'amDAI']:
            shape = 'DAI-collateral.svg'
        elif collateral == 'maWETH':
            shape = 'ETH-collateral.svg'
        elif collateral == 'maLINK':
            shape = 'LINK-collateral.svg'
        elif collateral in ['maUSDC', 'amUSDC']:
            shape = 'USDC-collateral.svg'
        elif collateral == 'maYFI':
            shape = 'YFI-collateral.svg'
        elif collateral == 'maUNI':
            shape = 'UNI-collateral.svg'
        elif collateral == 'maTUSD':
            shape = 'TUSD-collateral.svg'
        elif collateral in ['maUSDT', 'amUSDT']:
            shape = 'USDT-collateral.svg'
        elif collateral == 'amWMATIC':
            shape = 'Aavegotchi-H2-Collaterals-Polygon-Eyes.svg'
        elif collateral == 'amWBTC':
            shape = 'Aavegotchi-H2-Collaterals-wBTC-Eyes.svg'
        elif collateral == 'amWETH':
            shape = 'Aavegotchi-H2-Collaterals-wETH-Eyes.svg'
        else:
            shape = 'default.svg'  # default shape if collateral not recognized
    else:
        shape = 'default.svg'  # default shape if EYS not in the range

    # Determine color based on EYC and collateral
    if 0 <= EYC <= 1:
        color = '#ff04fc'
    elif 2 <= EYC <= 9:
        color = '#0864fc'
    elif 10 <= EYC <= 24:
        color = '#6024bc'
    elif 25 <= EYC <= 74:
        if collateral in ['maAAVE', 'amAAVE']:
            color = '#b6509e'
        elif collateral in ['maDAI', 'amDAI']:
            color = '#ff7d00'
        elif collateral == 'maWETH':
            color = '#64438e'
        elif collateral == 'maLINK':
            color = '#0000b9'
        elif collateral in ['maUSDC', 'amUSDC']:
            color = '#2664ba'
        elif collateral == 'maYFI':
            color = '#0074f9'
        elif collateral == 'maUNI':
            color = '#ff2a7a'
        elif collateral == 'maTUSD':
            color = '#282473'
        elif collateral in ['maUSDT', 'amUSDT']:
            color = '#26a17b'
        elif collateral == 'amWMATIC':
            color = '#824ee2'
        elif collateral == 'amWBTC':
            color = '#ff5e00'
        elif collateral == 'amWETH':
            color = '#000000'
        else:
            color = '#ffffff'  # default color if collateral not recognized
    elif 75 <= EYC <= 90:
        color = '#38848c'
    elif 91 <= EYC <= 97:
        color = '#f08c24'
    elif 98 <= EYC <= 99:
        color = '#58fcac'
    else:
        color = '#ffffff'  # default color if EYC not in the range

    return app.get_asset_url(shape), {'backgroundColor': color, 'opacity': 1, 'position': 'absolute', 'width': '50%', 'height': '100%'}



if __name__ == '__main__':
    app.run_server(debug=True)
