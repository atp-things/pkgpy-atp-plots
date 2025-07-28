from atpplots import BarDf

plot = BarDf(
    ticks=["1", "2", "3"],
    data_top=[4, 5, 6],
    title="Test Scatter Plot",
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
