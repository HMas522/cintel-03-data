"""
Purpose: Display outputs for Tips output dataset.

Choose the correct ui method for the type of output you want to display.
Provide the exact name of the server function that will provide the output.
"""
from shiny import ui


def get_tips_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Output (Not Yet Reactive)"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Tips Table"),
            ui.output_text("tips_record_count_string"),
            ui.output_table("tips_table"),
            ui.tags.hr(),
        ),
    )
