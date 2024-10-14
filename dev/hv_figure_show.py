import numpy as np

import atpplots

data_x = np.linspace(0, 10, 100)
data_y1 = [np.sin(2 * i) for i in data_x]
data_y2 = [np.cos(2 * i) for i in data_x]

data_vector_1 = atpplots.DataVector(
    data_x=data_x,
    data_y=data_y1,
    color="red",
    label="sin",
)
axis_y = atpplots.Axis(
    title="y-axis",
    unit="m",
    range_max=0.9,
    scale="linear",
)

plot_curve = atpplots.CurveDataVector(
    data_vector_1,
    title="Scatter plot",
    axis_y=axis_y,
)
plot_curve.show_holoviews()
