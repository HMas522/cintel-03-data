"""
Purpose: Display outputs for Health Care dataset.

Choose the correct ui method for the type of output you want to display.
Provide the exact name of the server function that will provide the output.
"""
from shiny import ui


def get_healthcare_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Output (Not Yet Reactive)"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Health Care Chart (Seaborn Scatter Plot)"),
            ui.output_plot("healthcare_plot"),
            ui.tags.hr(),
            ui.h3("Health Care Table"),
            ui.output_text("healthcare_record_count_string"),
            ui.output_table("healthcare_table"),
            ui.tags.hr(),
        ),
    )
