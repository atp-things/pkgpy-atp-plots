import holoviews as hv
import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure as bokeh_figure
from bokeh.transform import dodge

from .axis import Axis
from .figure import Figure


class BarDf(Figure):
    def __init__(
        self,
        data: pd.DataFrame,
        ticks: list[str],
        data_top: list[str],
        data_bottom: list[str | None] | None = None,
        title: str | None = None,
        axis_x: str | Axis | dict = "X",
        axis_y: str | Axis | dict = "Y",
        width: int | None = None,
        height: int | None = None,
        color: str | list[str] = "blue",
        labels: list[str] | None = None,
        bar_width: float = 0.2,
    ):
        # inheritances
        Figure.__init__(
            self,
            title=title,
            width=width,
            height=height,
        )
        # Attributes
        self.data: pd.DataFrame = data
        self.ticks: list[str] = ticks
        self.data_top: list[str] = data_top
        if data_bottom is None:
            data_bottom = [None] * len(data_top)
        self.data_bottom: list[str | None] = data_bottom

        self.labels: list[str] | None = labels

        self.axis_x = Axis.init(axis_x)
        self.axis_y = Axis.init(axis_y)
        self.color: str | list[str] = color
        self.bar_width: float = bar_width

        return None

    def to_holoviews(self):
        raise NotImplementedError(
            "BarDf does not support Holoviews conversion. Use to_bokeh() instead."
        )
        # Prepare data
        self.data["ticks"] = self.data[self.ticks].apply(tuple, axis=1)
        # Create bars
        bars = []
        for _i, data_top in enumerate(self.data_top):
            bars.append(
                hv.Bars(
                    self.data,
                    kdims=["ticks"],
                    vdims=[data_top],
                    # label=self.labels[i] if self.labels is not None else None,
                ).opts(
                    # color=self.color[i] if self.color is not None else None,
                )
            )

        return hv.Overlay(bars).opts(
            width=self.width,
            height=self.height,
            title=self.title,
        )

    def to_bokeh(self):
        # Prepare data
        self.data["ticks"] = self.data[self.ticks].apply(tuple, axis=1)
        source = ColumnDataSource(self.data)
        numberof_bars = len(self.data_top)
        bar_offset = self.bar_width / 2 * (numberof_bars - 1)

        # Create figure
        fig: bokeh_figure = bokeh_figure(
            x_range=FactorRange(*self.data["ticks"].unique()),
            title=self.title,
            width=self.width,
            height=self.height,
            # toolbar_location=None,
            # tools="",
            y_axis_type=self.axis_y.scale,
        )
        fig.xgrid.grid_line_color = None
        fig.legend.location = "top_left"
        fig.legend.orientation = "horizontal"

        fig.xaxis.axis_label = self.axis_x.label
        fig.yaxis.axis_label = self.axis_y.label
        if self.axis_y.range_min is not None:
            fig.y_range.start = self.axis_y.range_min
        if self.axis_y.range_max is not None:
            fig.y_range.end = self.axis_y.range_max

        # Add bars
        for i, data_top in enumerate(self.data_top):
            label = self.labels[i] if isinstance(self.labels, list) else data_top
            data_bottom = self.data_bottom[i] if self.data_bottom[i] is not None else 0
            color = self.color[i] if isinstance(self.color, list) else self.color

            fig.vbar(
                source=source,
                x=dodge("ticks", i * self.bar_width - bar_offset, range=fig.x_range),
                top=data_top,
                bottom=data_bottom,
                width=self.bar_width,
                legend_label=label,
                color=color,
            )

        return fig
