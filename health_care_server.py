""" 
Purpose: Provide reactive output for the Penguins dataset.

- Use inputs from the UI Sidebar to filter the dataset.
- Update reactive outputs in the UI Main Panel.

Matching the IDs in the UI Sidebar and function/output names in the UI Main Panel
to this server code is critical. They are case sensitive and must match exactly.

"""
import pathlib
from shiny import render
import pandas as pd
import seaborn as sns

from util_logger import setup_logger

logger, logname = setup_logger(__name__)


def get_health_care_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    path_to_data = (
        pathlib.Path(__file__).parent.joinpath("data").joinpath("healthexp.csv")
    )
    original_df = pd.read_excel(path_to_data)
    total_count = len(original_df)

    @output
    @render.table
    def health_care_table():
        return original_df

    @output
    @render.text
    def health_care_record_count_string():
        message = f"Showing {total_count} records"
        logger.debug(f"filter message: {message}")
        return message

    @output
    @render.text
    def health_care_filter_string():
        input_Life_Expectancy_range = input.Life_Expectancy_range()
        input_min = input_Life_Expectancy_range[0]
        input_max = input_Life_Expectancy_range[1]
        filter_string = f"Life_Expectancy between {input_min} and {input_max}"
        return filter_string

    @output
    @render.text
    def health_care_filtered_record_count_string():
        logger.debug("Triggered penguin_filter_record_count_string")
        df = original_df.copy()
        input_Life_Expectancy_range = input.Life_Expectancy_range()
        input_min = input_Life_Expectancy_range[0]
        input_max = input_Life_Expectancy_range[1]
        condition1 = df["Life_Expectancy"] >= input_min
        condition2 = df["Life_Expectancy"] <= input_max
        filter = condition1 & condition2
        df = df[filter]
        filtered_records = len(df)
        record_count_string = (
            f"Filter shows {filtered_records} of {total_count} records"
        )
        return record_count_string

    @output
    @render.table
    def health_care_filtered_table():
        logger.debug("Triggered health_care_filtered_table")
        df = original_df.copy()
        input_Life_Expectancy_range = input.Life_Expectancy_RANGE()
        input_min = input_Life_Expectancy_range[0]
        input_max = input_Life_Expectancy_range[1]
        condition1 = df["Life_Expectancy"] >= input_min
        condition2 = df["Life_Expectancy"] <= input_max
        filter = condition1 & condition2
        df = df[filter]
        return df

    @output
    @render.text
    def health_care_stats():
        """Generate and present summary statistics using pandas describe() method
        and by calling value_counts() on the country column."""

        desc = original_df.describe()
        formatted_desc = desc.applymap("{0:.2f}".format)
        part1 = formatted_desc.to_string()

        # Generate value counts for 'species' column
        value_counts = original_df["Country"].value_counts().to_string()
        blank_line = "\n\n"
        part2 = "Value Counts for Country" + blank_line + value_counts
        reply = part1 + blank_line + part2 + blank_line
        return reply

    @output
    @render.plot
    def health_care_pairplots():
        """Seaborn pairplot creates a grid of plots -
        each variable shares the
        y-axes across the row and the x-axes across a column.
        Diagonals show the distribution of data for that column.
        Seaborn charts aren't interactive, but they look nice.
        Don't worry about the formatting -
        we'll look at more interactive options in the next module."""

        df = original_df

        # Drop the 'Unnamed' index column
        df = df.drop(columns=["Year"])

        sns.set_theme(style="ticks")
        pairplot_grid = sns.pairplot(df, hue="Country")
        return pairplot_grid

    @output
    @render.plot
    def health_care_scatterplot1():
        """
        Use Seaborn to make a quick scatterplot.
        Provide a pandas DataFrame and the names of the columns to plot.
        Learn more at https://stackabuse.com/seaborn-scatter-plot-tutorial-and-examples/
        """

        df = original_df.copy()
        input_Life_Expectancy_range = input.Life_Expectancy_RANGE()
        input_min = input_Life_Expectancy_range[0]
        input_max = input_Life_Expectancy_range[1]
        condition1 = df["Life_Expectancy"] >= input_min
        condition2 = df["Life_Expectancy"] <= input_max
        filter = condition1 & condition2
        df = df[filter]

        plt = sns.scatterplot(
            data=df,
            x="Spending_USD",
            y="Life_Expectancy",
            hue="health_care",
            style="Year",
        )
        return plt

    # return a list of function names for use in reactive outputs
    return [
        health_care_table,
        health_care_record_count_string,
        health_care_stats,
        health_care_table,
        health_care_record_count_string,
        health_care_pairplots,
        health_care_scatterplot1,
    ]
