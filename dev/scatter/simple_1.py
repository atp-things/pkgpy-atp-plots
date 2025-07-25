from atpplots import Scatter

plot = Scatter(
    data_x=[1, 2, 3],
    data_y=[4, 5, 6],
    title="Test Scatter Plot",
    color="blue",
)
# switch case
select = 3
match select:
    case 1:
        plot.show_bokeh()
    case 2:
        plot.show_holoviews()
    case 3:
        plot.show_plotly()
