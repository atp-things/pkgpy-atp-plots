import holoviews as hv
import numpy as np


class AtpHistogramPlot:
    def __init__(
        self,
        counts: list | np.ndarray | None = None,
        bin_edges: list | np.ndarray | None = None,
        title: str = "Histogram",
        axis_x_label: str = "X",
        axis_y_label: str = "Y",
        width: int = 1000,
        height: int = 600,
    ):
        self.hist: list | np.ndarray | None = counts
        self.bin_edges: list | np.ndarray | None = bin_edges
        self.title: str = title
        self.axis_x_label: str = axis_x_label
        self.axis_y_label: str = axis_y_label
        self.width: int = width
        self.height: int = height

        return None

    def get_hv(self) -> hv.Histogram:
        ret = hv.Histogram(
            (self.hist, self.bin_edges),
            kdims=[self.axis_x_label],
            vdims=[self.axis_y_label],
        ).opts(
            width=self.width,
            height=self.height,
            title=self.title,
        )

        return ret
