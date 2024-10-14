import holoviews as hv
import numpy as np
from bokeh.plotting import show

import atpplots

hv.extension("bokeh")
data_x = np.linspace(0, 10, 100)
data_y = [np.sin(2 * i) for i in data_x]

data_vector_1 = atpplots.DataVector(
    data_x=data_x,
    data_y=data_y,
    color="red",
    label="sin",
)

plot_scatter = atpplots.Scatter(
    data_x,
    data_y,
    title="Scatter plot",
    color="red",
)

plot_curve = atpplots.CurveDataVector(data_vector_1, title="Scatter plot")
plot_curve.show_holoviews()

# show(hv.render(plot_scatter.to_holoviews() * plot_curve.to_holoviews()))
