"""
Purpose: Display outputs for  health_care dataset.

Choose the correct ui method for the type of output you want to display.
Provide the exact name of the server function that will provide the output.

"""
from shiny import ui


def get_health_care_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("health_care: Seaborn Scatter Plot (filtered by Body Mass)"),
            ui.output_plot("health_care_scatterplot1"),
            ui.tags.hr(),
            ui.h3("Filtered health_care Table (filtered by Body Mass)"),
            ui.output_text("health_care_filtered_record_count_string"),
            ui.output_table("health_care_filtered_table"),
            ui.tags.hr(),
            ui.h3("health_care: Seaborn Pair Plots"),
            ui.output_plot("health_care_pairplots"),
            ui.tags.hr(),
            ui.h3("health_care Table Summary Statistics"),
            ui.output_text_verbatim("health_care_stats"),
            ui.tags.hr(),
            ui.h3("health_care Table"),
            ui.output_text("health_care_record_count_string"),
            ui.output_table("health_care_table"),
            ui.tags.hr(),
        ),
    )
