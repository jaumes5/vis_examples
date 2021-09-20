import plotly.express as px
import dash
from dash import dcc, html
from skimage import data

import plotly.graph_objects as go
import numpy as np


def three_d_fig():
    x, y, z = np.mgrid[-8:8:40j, -8:8:40j, -8:8:40j]
    values = np.sin(x * y * z) / (x * y * z)

    fig = go.Figure(
        data=go.Volume(
            x=x.flatten(),
            y=y.flatten(),
            z=z.flatten(),
            value=values.flatten(),
            isomin=0.1,
            isomax=0.8,
            opacity=0.1,  # needs to be small to see through all surfaces
            surface_count=17,  # needs to be a large number for good volume rendering
        )
    )
    fig.update_layout(dragmode="drawrect")
    return fig


def simple_anotation_2d():
    img = data.chelsea()
    fig = px.imshow(img)
    fig.update_layout(dragmode="drawrect")
    return fig


if __name__ == "__main__":
    config = {
        "modeBarButtonsToAdd": [
            "drawline",
            "drawopenpath",
            "drawclosedpath",
            "drawcircle",
            "drawrect",
            "eraseshape",
        ]
    }
    app = dash.Dash(__name__)
    app.layout = html.Div(
        [
            html.Div(
                [
                    html.H3("Drag and draw 2D annotations"),
                    dcc.Graph(figure=simple_anotation_2d(), config=config),
                ]
            ),
            html.Div(
                [
                    html.H3("3D object"),
                    dcc.Graph(figure=three_d_fig()),  # The previous config doesn't work for 3D objects
                ]
            ),
        ]
    )
    app.run_server(debug=True)
