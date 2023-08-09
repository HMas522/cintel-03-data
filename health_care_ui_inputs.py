"""
Purpose: Provide user interaction options for the Penguins dataset.

 - Choose checkboxes when the options are independent of each other.
 - Choose radio buttons when a set of options are mutually exclusive.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""

from shiny import ui


def get_penguins_inputs():
    return ui.panel_sidebar(
        ui.h2("Health Care Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "Life_Expectancy_RANGE",
            "Life_Expectancy (years)",
            min=70,
            max=90,
            value=[70, 90],
        ),
        ui.input_numeric("Spending_USD", "Max Spending_USD (dollars):", value=10000),
        ui.input_checkbox("HealthCare_Country_Germany", "Germany", value=True),
        ui.input_checkbox("HealthCare_Country_France", "France", value=True),
        ui.input_checkbox("HealthCare_Country_Japan", "USA", value=True),
        ui.input_checkbox("HealthCare_Country_Canada", "Canada", value=True
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
