""" 
Purpose: Provide reactive output for the Tips dataset.

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

        # Set the reactive value
    reactive_df.set(filtered_df)

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

    # return a list of function names for use in reactive outputs
    return [
        tips_record_count_string,
        tips_filtered_table,
    ]