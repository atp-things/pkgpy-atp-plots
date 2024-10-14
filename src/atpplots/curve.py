import holoviews as hv
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from .axis import Axis
from .datavector import DataVector
from .figure import Figure

hv.extension("bokeh")


class Curve(Figure):
    def __init__(
        self,
        data_x: list | np.ndarray | None = None,
        data_y: list | np.ndarray | None = None,
        title: str | None = None,
        axis_x: str | Axis | dict = "X",
        axis_y: str | Axis | dict = "Y",
        width: int | None = None,
        height: int | None = None,
        color: str = "blue",
        label: str = "",
        interpolation: str = "linear",
    ):
        if interpolation not in ["linear", "ffill", "bfill"]:
            raise ValueError(
                f"Interpolation method '{interpolation}' is not supported."
            )
        # inheritances
        Figure.__init__(
            self,
            title=title,
            width=width,
            height=height,
        )

        self.data_x: list | np.ndarray | None = data_x
        self.data_y: list | np.ndarray | None = data_y
        self.axis_x = Axis.init(axis_x)
        self.axis_y = Axis.init(axis_y)
        self.color: str = color
        self.label: str = label

        self.interpolation: str = interpolation

        return None

    def to_holoviews(self) -> hv.Scatter:
        ret = hv.Curve(
            (self.data_x, self.data_y),
            kdims=[self.axis_x.hv_dimension],
            vdims=[self.axis_y.hv_dimension],
            label=self.label,
        ).opts(
            width=self.width,
            height=self.height,
            title=self.title,
            color=self.color,
            shared_axes=False,
            interpolation=interpolation_to_holoviews(interpolation=self.interpolation),
        )

        return ret


def interpolation_to_holoviews(interpolation: str) -> str:
    # TODO: obsolete
    if interpolation == "linear":
        return "linear"
    elif interpolation == "ffill":
        return "steps-post"
    elif interpolation == "bfill":
        return "steps-pre"
    else:
        raise ValueError(f"Interpolation method '{interpolation}' is not supported.")


class CurveDataVector(Figure):
    def __init__(
        self,
        data_vectors: DataVector | list[DataVector],
        axis_x: str | Axis | dict = "X",
        axis_y: str | Axis | dict = "Y",
        **kwargs,
    ):
        # inheritances
        Figure.__init__(
            self,
            **kwargs,
        )

        self.axis_x = Axis.init(axis_x)
        self.axis_y = Axis.init(axis_y)

        if not isinstance(data_vectors, list):
            data_vectors = [data_vectors]
        self.data_vectors = data_vectors

        return None

    def to_holoviews(self) -> hv.Overlay:
        ret = []

        for data_vector in self.data_vectors:
            curve = data_vector.to_holoviews_scatter(
                kdims=[self.axis_x.hv_dimension],
                vdims=[self.axis_y.hv_dimension],
            )

            ret.append(curve)

        return hv.Overlay(ret).opts(
            width=self.width,
            height=self.height,
            title=self.title,
        )

    def _plotly_figure(self) -> go.Figure:
        fig = go.Figure()
        fig.update_layout(
            title=self.title,
            width=self.width,
            height=self.height,
            showlegend=self.showlegend,
        )
        fig.update_xaxes(
            title_text=self.axis_x.label,
            range=self.axis_x.range,
            type=self.axis_x.scale,
        )
        fig.update_yaxes(
            title_text=self.axis_y.label,
            range=self.axis_y.range,
            type=self.axis_y.scale,
        )
        return fig

    def to_plotly(self) -> go.Figure:
        fig = self._plotly_figure()

        for data_vector in self.data_vectors:
            fig.add_trace(data_vector.to_plotly_scatter())

        return fig
