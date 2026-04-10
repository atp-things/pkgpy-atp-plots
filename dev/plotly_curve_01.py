import numpy as np

import atpplots

data_x = np.linspace(0, 10, 100)
data_y_1 = [np.sin(2 * i) for i in data_x]
data_y_2 = [np.cos(2 * i) for i in data_x]


plot_curve = atpplots.Curve(
    data_x,
    data_y_1,
    title="Scatter plot",
    interpolation="bfill",
)
figure = plot_curve.to_plotly()
figure.show()
