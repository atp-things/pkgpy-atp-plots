import holoviews as hv
import numpy as np

from .axis import Axis
from .figure import Figure


class ConfusionMatrix(Figure):
    def __init__(
        self,
        conf_matrix_list_tuple: list[tuple],
        ticks: list[str],
        title: str | None = None,
        axis_x: str | Axis | dict = "X",
        axis_y: str | Axis | dict = "Y",
        width: int | None = None,
        height: int | None = None,
        tick_not_predicted: list | None = None,
    ):
        # inheritances
        Figure.__init__(
            self,
            title=title,
            width=width,
            height=height,
        )
        self.axis_x = Axis.init(axis_x)
        self.axis_y = Axis.init(axis_y)
        self.conf_matrix_list_tuple: list[tuple] = conf_matrix_list_tuple
        self.tick_not_predicted: list | None = tick_not_predicted

        return None

    def to_holoviews(self) -> hv.Overlay:
        heatmap = hv.HeatMap(
            self.conf_matrix_list_tuple,
            kdims=[self.axis_x.hv_dimension, self.axis_y.hv_dimension],
            # vdims=[label_z],
        ).opts(
            tools=["hover"],
            width=self.width,
            height=self.height,
        )

        hv_confusing_matrix = (
            heatmap
            * hv.Labels(heatmap).opts(padding=0, text_color="red")
            * hv.Labels([t for t in self.conf_matrix_list_tuple if t[0] == t[1]]).opts(
                padding=0,
                text_color="green",
            )
            * hv.Labels(
                [
                    t
                    for t in self.conf_matrix_list_tuple
                    if t[0] in self.tick_not_predicted
                ]
            ).opts(
                padding=0,
                text_color="orange",
            )
        ).opts(title=self.title)

        return hv_confusing_matrix
