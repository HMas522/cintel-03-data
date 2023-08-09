"""
Purpose: Use Python to create a continuous intelligence and 
interactive analytics dashboard using Shiny for Python.

Each Shiny app has two parts: 

- a user interface app_ui object (similar to the HTML in a web page) 
- a server function that provides the logic for the app (similar to JS in a web page).

"""
import shinyswatch
from shiny import App, ui, render

from tips_server import get_tips_server_functions
from tips_ui_inputs import get_tips_inputs
from tips_ui_outputs import get_tips_outputs

from healthcare_server import get_healthcare_server_functions
from healthcare_ui_inputs import get_healthcare_inputs
from healthcare_ui_outputs import get_healthcare_outputs

from util_logger import setup_logger

logger, logname = setup_logger(__name__)

app_ui = ui.page_navbar(
    shinyswatch.theme.vapor(),
    ui.nav(
        "Home",
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.h2("Sidebar Panel"),
                ui.tags.hr(),
                ui.h3("User Interaction Here"),
                ui.input_text("name_input", "Enter your name", placeholder="Your Name"),
                ui.input_text(
                    "language_input",
                    "Enter your favorite language(s)",
                    placeholder="Favorite Programming Language(s)",
                ),
                ui.tags.hr(),
            ),
            ui.panel_main(
                ui.h2("New Data Exploration Tabs (see above)"),
                ui.tags.hr(),
                ui.tags.ul(
                    ui.tags.li(
                        "To explore Restaurant Tip dataset, click the 'Tips' tab."
                    ),
                    ui.tags.li(
                        "To explore the Health Care Dataset, click the 'Health_Care' tab."
                    ),
                ),
                ui.tags.hr(),
                ui.h2("Main Panel with Reactive Output"),
                ui.tags.hr(),
                ui.output_text_verbatim("welcome_output"),
                ui.output_text_verbatim("insights_output"),
                ui.tags.hr(),
            ),
        ),
    ),
    ui.nav(
        "Tips",
        ui.layout_sidebar(
            get_tips_inputs(),
            get_tips_outputs(),
        ),
    ),
    ui.nav(
        "Health Care",
        ui.layout_sidebar(
            get_healthcare_inputs(),
            get_healthcare_outputs(),
        ),
    ),
    ui.nav(ui.a("About", href="https://github.com/HMas522")),
    ui.nav(ui.a("GitHub", href="https://github.com/HMas522/cintel-03-data")),
    ui.nav(ui.a("App", href="https://HMas522.shinyapps.io/cintel-03-data/")),
    ui.nav(ui.a("Examples", href="https://shinylive.io/py/examples/")),
    ui.nav(ui.a("Themes", href="https://bootswatch.com/")),
    title=ui.h1("HMas522 Dashboard"),
)


def server(input, output, session):
    """Define functions to create UI outputs."""

    @output
    @render.text
    def welcome_output():
        user = input.name_input()
        welcome_string = f"Greetings {user}!"
        return welcome_string

    @output
    @render.text
    def insights_output():
        answer = input.language_input()
        count = len(answer)
        language_string = f"You like {answer}. That takes {count} characters"
        return language_string

    get_tips_server_functions(input, output, session)
    get_healthcare_server_functions(input, output, session)


app = App(app_ui, server)
