import holoviews as hv
import numpy as np
from bokeh.plotting import show

import atpplots

hv.extension("bokeh")
data_x = np.linspace(0, 10, 100)
data_y = [np.sin(2 * i) for i in data_x]

plot_scatter = atpplots.Scatter(
    data_x,
    data_y,
    title="Scatter plot",
    color="red",
)

plot_curve = atpplots.Curve(
    data_x,
    data_y,
    title="Scatter plot",
    interpolation="bfill",
)


show(hv.render(plot_scatter.to_holoviews() * plot_curve.to_holoviews()))
