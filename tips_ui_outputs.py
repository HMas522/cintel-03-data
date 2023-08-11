"""
Purpose: Display output for MT Cars dataset.

@imports shiny.ui as ui
@imports shinywidgets.output_widget for interactive charts
"""
from shiny import ui
from shinywidgets import output_widget


def get_mtcars_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Tips: Charts"),
            output_widget("tips_output_widget1"),
            ui.output_plot("tips_plot1"),
            ui.output_plot("tips_plot2"),
            ui.tags.hr(),
            ui.h3("Filtered Tips Table"),
            ui.output_text("tips_record_count_string"),
            ui.output_table("tips_filtered_table"),
            ui.tags.hr(),
        ),
    )