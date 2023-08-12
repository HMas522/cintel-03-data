"""
Purpose: Provide user interaction options for MT Cars dataset.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""
from shiny import ui


def get_tips_inputs():
    return ui.panel_sidebar(
        ui.h2("Tips Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "Tips_USD_RANGE",
            "Tips (USD)",
            min=1,
            max=35,
            value=[1, 35],
        ),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Tips Table"),
            ui.tags.p("Description of each field in the table:"),
            ui.tags.ul(
                ui.tags.li("total_bill: How most Tips are calculated"),
                ui.tags.li("tip: Percentage of the total bill"),
                ui.tags.li("sex: Gender of service staff"),
                ui.tags.li("smoker: Smoking section?"),
                ui.tags.li("day: Day of the week"),
                ui.tags.li("time: Lunch or Dinner rush"),
                ui.tags.li("size: number in party"),
            ),
        ui.output_table("tips_table"),
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )