import pandas as pd

from atpplots import Axis, BarDf

df = pd.DataFrame(
    {
        "quarter": [
            "Q1",
            "Q1",
            "Q1",
            "Q2",
            "Q2",
            "Q2",
            "Q3",
            "Q3",
            "Q3",
            "Q4",
            "Q4",
            "Q4",
        ],
        "month": [
            "jan",
            "feb",
            "mar",
            "apr",
            "may",
            "jun",
            "jul",
            "aug",
            "sep",
            "oct",
            "nov",
            "dec",
        ],
        "west": [5, 3, 4, 2, 4, 6, 7, -8, 6, 9, 5, 4],
        "east": [5, 1, 9, 4, 5, 4, 7, 7, 7, 6, 6, 7],
    }
)


plot = BarDf(
    data=df,
    ticks=["quarter", "month"],
    data_top=["west", "east"],
    # data_bottom=[None, "west"],
    labels=["West", "East"],
    color=["blue", "red"],
    # color="red",
    title="Test Bar Plot",
    axis_x=Axis(title="Time", unit="quarters"),
    axis_y=Axis(
        title="Count",
        unit="cats",
        # scale="log",
        range_min=0,
        # range_max=5,
    ),
)
# switch case
select = 2
match select:
    case 1:
        plot.show_bokeh()
    case 2:
        plot.show_holoviews()
    case 3:
        plot.show_plotly()
