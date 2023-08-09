""" 
Purpose: Provide reactive output for Health Care dataset.

Matching the IDs in the UI Sidebar and function/output names in the UI Main Panel
to this server code is critical. They are case sensitive and must match exactly.

"""
import pathlib
from shiny import render
import pandas as pd
import seaborn as sns

from util_logger import setup_logger

logger, logname = setup_logger(__name__)


def get_healthcare_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    path_to_data = pathlib.Path(__file__).parent.joinpath("data").joinpath("healthexp.csv")
    original_df = pd.read_csv(path_to_data)

    # Use the len() function to get the number of rows in the DataFrame.
    total_count = len(original_df)

    @output
    @render.table
    def healthcare_table():
        return original_df

    @output
    @render.text
    def healthcare_record_count_string():
        message = f"Showing {total_count} records"
        logger.debug(f"filter message: {message}")
        return message

    @output
    @render.plot
    def healthcare_plot():
        """
        Use Seaborn to make a quick scatterplot.
        Provide a pandas DataFrame and the names of the columns to plot.
        Learn more at https://stackabuse.com/seaborn-scatter-plot-tutorial-and-examples/
        """
        plt = sns.scatterplot(
            data=original_df,
            x="Spending_USD",
            y="Life_Expectancy",
        )
        return plt

    # return a list of function names for use in reactive outputs
    return [
        healthcare_table,
        healthcare_record_count_string,
        healthcare_plot,
    ]
