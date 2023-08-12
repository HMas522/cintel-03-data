""" 
Purpose: Provide reactive output for the MT Cars dataset.

- Use inputs from the UI Sidebar to filter the dataset.
- Update reactive outputs in the UI Main Panel.

Matching the IDs in the UI Sidebar and function/output names in the UI Main Panel
to this server code is critical. They are case sensitive and must match exactly.

"""
import pathlib
from shiny import render, reactive
import matplotlib.pyplot as plt
import pandas as pd
from plotnine import aes, geom_point, ggplot, ggtitle
from shinywidgets import render_widget
import plotly.express as px

from util_logger import setup_logger

logger, logname = setup_logger(__name__)


def get_tips_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    p = pathlib.Path(__file__).parent.joinpath("data").joinpath("tips.csv")
    # logger.info(f"Reading data from {p}")
    original_df = pd.read_csv(p)
    total_count = len(original_df)

    reactive_df = reactive.Value()

    @output
    @render.text
    def tips_record_count_string():
        filtered_df = reactive_df.get()
        filtered_count = len(filtered_df)
        message = f"Showing {filtered_count} of {total_count} records"
        # logger.debug(f"filter message: {message}")
        return message

    @output
    @render.table
    def tips_filtered_table():
        filtered_df = reactive_df.get()
        return filtered_df

    @output
    @render_widget
    def tips_output_widget1():
        df = reactive_df.get()
        plotly_express_plot = px.scatter(df, x="total_bill", y="tip", color="time", size="sex")
        plotly_express_plot.update_layout(title="Tips with Plotly Express")
        return plotly_express_plot

    @output
    @render.plot
    def tips_plot1():
        df = reactive_df.get()
        matplotlib_fig, ax = plt.subplots()
        plt.title("Tips with matplotlib")
        ax.scatter(df["time"], df["tip"])
        return matplotlib_fig

    @output
    @render.plot
    def tips_plot2():
        df = reactive_df.get()
        plotnine_plot = (
            ggplot(df, aes("time", "time"))
            + geom_point()
            + ggtitle("Tips with plotnine")
        )

        return plotnine_plot

    # return a list of function names for use in reactive outputs
    return [
        tips_record_count_string,
        tips_filtered_table,
        tips_output_widget1,
        tips_plot1,
        tips_plot2,
    ]