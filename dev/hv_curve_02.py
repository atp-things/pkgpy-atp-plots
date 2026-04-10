import holoviews as hv
import numpy as np
from bokeh.plotting import show

import atpplots

data_x = np.linspace(0, 10, 100)
data_y_1 = [np.sin(2 * i) for i in data_x]
data_y_2 = [np.cos(2 * i) for i in data_x]
data_y_3 = [np.cos(4 * i) for i in data_x]

plot_curve_1 = atpplots.Curve(
    data_x,
    data_y_1,
    label="sin",
    interpolation="bfill",
)
plot_curve_2 = atpplots.Curve(
    data_x,
    data_y_2,
    label="cos",
    # interpolation="bfill",
)
plot_scatter = atpplots.Scatter(
    data_x,
    data_y_3,
    label="2cos",
    # interpolation="bfill",
)
show(
    hv.render(
        hv.Overlay(
            [
                plot_curve_1.to_holoviews(),
                plot_curve_2.to_holoviews(),
                plot_scatter.to_holoviews(),
            ]
        ).opts(
            title="Scatter plot2",
        )
    )
)
