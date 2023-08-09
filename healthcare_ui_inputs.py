"""
Purpose: Provide user interaction options for the MT Cars dataset.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""
from shiny import ui


def get_mtcars_inputs():
    return ui.panel_sidebar(
        ui.h2("Health Care Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "Life_Expectancy_RANGE",
            "Life_Expectancy (Years)",
            min=60,
            max=90,
            value=[60, 90],
        ),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Health Care Table"),
            ui.tags.p("Description of each field in the table:"),
            ui.tags.ul(
                ui.tags.li("Years: 1970 to 2020"),
                ui.tags.li("Countries: six"),
                ui.tags.li("USD: Currency US dollar"),
                ui.tags.li("Life_Expectancy: Year of Passing"),
            ),
            ui.output_table("healthcare_table"),
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
