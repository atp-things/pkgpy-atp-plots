import holoviews as hv
import numpy as np

from ..axis import Axis


class Histogram:
    def __init__(
        self,
        counts: list | np.ndarray | None = None,
        bin_edges: list | np.ndarray | None = None,
        title: str = "Histogram",
        axis_x: str | Axis | dict = "X",
        axis_y: str | Axis | dict = "Y",
        width: int = 1000,
        height: int = 600,
        color: str = "blue",
    ):
        self.hist: list | np.ndarray | None = counts
        self.bin_edges: list | np.ndarray | None = bin_edges
        self.title: str = title
        self.axis_x = Axis.init(axis_x)
        self.axis_y = Axis.init(axis_y)
        self.width: int = width
        self.height: int = height
        self.color: str = color

        return None

    def set_axis(self, axis: str | Axis | dict) -> Axis:
        if isinstance(axis, Axis):
            return axis
        elif isinstance(axis, str):
            return Axis(id=axis, title=axis)
        elif isinstance(axis, dict):
            return Axis(**axis)
        else:
            raise ValueError(f"Invalid axis type: {type(axis)}")

    def to_holoviews(self) -> hv.Histogram:
        ret = hv.Histogram(
            (self.hist, self.bin_edges),
            kdims=[self.axis_x.hv_dimension],
            vdims=[self.axis_y.hv_dimension],
        ).opts(
            width=self.width,
            height=self.height,
            title=self.title,
            color=self.color,
        )

        return ret


class Bars:
    def __init__(
        self,
        counts: list | np.ndarray,
        ticks: list[str],
        title: str = "Histogram",
        axis_x: str | Axis | dict = "X",
        axis_y: str | Axis | dict = "Y",
        width: int = 1000,
        height: int = 600,
        color: str | list[str] = "blue",
        labels: list[str] | None = None,
    ):
        self.counts: list | np.ndarray = counts
        self.ticks: list[str] = ticks
        self.labels: list[str] | None = labels

        self.title: str = title
        self.axis_x = Axis.init(axis_x)
        self.axis_y = Axis.init(axis_y)
        self.width: int = width
        self.height: int = height
        self.color: str | list[str] = color

        return None

    def to_holoviews(self) -> hv.Overlay:
        bars = []
        for i in range(len(self.counts)):
            bars.append(
                hv.Bars(
                    [(self.ticks[i], self.counts[i])],
                    self.axis_x.hv_dimension,
                    vdims=[self.axis_y.hv_dimension],
                    label=self.labels[i] if self.labels is not None else None,
                ).opts(
                    color=self.color[i] if self.color is not None else None,
                )
            )

        return hv.Overlay(bars).opts(
            width=self.width,
            height=self.height,
            title=self.title,
        )
