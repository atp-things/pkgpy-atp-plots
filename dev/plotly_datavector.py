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
data_vector_2 = atpplots.DataVector(
    data_x=data_x,
    data_y=data_y2,
    color="blue",
    label="cos",
)


plot_curve = atpplots.CurveDataVector(
    [data_vector_1, data_vector_2],
    title="Scatter plot",
)
plot_curve.show_plotly()
