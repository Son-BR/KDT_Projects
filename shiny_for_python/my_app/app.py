import pandas as pd
from io import StringIO

from shiny import App, render, ui


app_ui = ui.page_fluid(
    ui.input_text_area("csv_text", "CSV Text", value="a, b\n1, 2"),
    ui.output_table("parsed_data"),
)

def server(input, output, session):
    @output
    @render.table
    def parsed_data():
        file_text = StringIO(input.csv_text())
        data = pd.read_csv(file_text)
        return data

# This is a shiny.App object. It must be named `app`.
app = App(app_ui, server)
