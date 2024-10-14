import numpy as np

import atpplots

data_x = np.linspace(0, 10, 100)
data_y = [np.sin(2 * i) for i in data_x]


plot_curve = atpplots.Curve(
    data_x,
    data_y,
    title="Scatter plot",
    interpolation="bfill",
)
figure = plot_curve.to_plotly()
figure.show()
