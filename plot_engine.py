from llama_index.core.tools import FunctionTool
import os
import plotly.graph_objects as go


def make_scatter_plot(title, x, y, x_title, y_title):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=x, y=y, mode='lines')
    )
    fig.update_layout(plot_bgcolor='white',
                      showlegend=False,
                      title=title,
                      yaxis_title=y_title,
                      xaxis_title=x_title)
    fig.show()

    return "scatter plot generated"

scatter_plot_engine = FunctionTool.from_defaults(
    fn=make_scatter_plot,
    name="scatter_plot_maker",
    description="this tool makes a scatter plot for the user given plot title, \
        x and y  values and  and y axis titles",
)
