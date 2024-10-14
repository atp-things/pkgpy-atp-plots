import holoviews as hv
import numpy as np
from bokeh.plotting import show

import atpplots

hv.extension("bokeh")
data_x = np.linspace(0, 10, 100)
data_y1 = [np.sin(2 * i) for i in data_x]
data_y2 = [np.cos(2 * i) for i in data_x]


data_vector_1 = atpplots.DataVector(
    data_x=data_x,
    data_y=data_y1,
    color="red",
    label="sin",
)
data_vector_2 = atpplots.DataVector(
    data_x=data_x,
    data_y=data_y2,
    color="blue",
    label="cos",
)

plot_scatter1 = atpplots.Scatter(
    data_x,
    data_y1,
    title="Scatter plot",
    color="red",
)
plot_scatter2 = atpplots.Scatter(
    data_x,
    data_y2,
    title="Scatter plot",
    color="red",
)


plot_curve = atpplots.CurveDataVector(
    data_vector_1,
    title="Scatter plot",
)
# plot_curve = atpplots.CurveDataVector(
#     [data_vector_1, data_vector_2],
#     title="Scatter plot",
# )

show(
    hv.render(
        plot_scatter1.to_holoviews()
        * plot_scatter2.to_holoviews()
        * plot_curve.to_holoviews()
    )
)
