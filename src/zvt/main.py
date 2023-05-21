import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash import dcc
from furl import furl

from zvt import init_plugins
from zvt.ui import zvt_app
from zvt.ui.apps import factor_app


def debug_layout():
    layout = html.Div([
        html.Div(children='Hello World')
    ])

def serve_layout():
    layout = html.Div(
        children=[
            # banner
            html.Div(className="zvt-banner", children=html.H2(className="h2-title", children="ZVT")),
            dbc.CardHeader(
                dbc.Tabs(
                    [dbc.Tab(label="factor", tab_id="tab-factor", label_style={}, tab_style={"width": "100px"})],
                    id="card-tabs",
                    # card=True,
                    active_tab="tab-factor",
                )
            ),
            dbc.CardBody(html.P(id="card-content", className="card-text")),
            dcc.Location(id = "url", refresh=False)
        ]
    )

    return layout


@zvt_app.callback(Output("card-content", "children"), [Input("card-tabs", "active_tab"), Input("url", "href")])
def tab_content(active_tab, href):
    f = furl(href)
    trader = f.args.get("trader", "followiitrader")
    provider = f.args.get("provider")
    entity = f.args.get("entity")
    entityType = f.args.get("entityType", "stock")
    level = f.args.get("level", "1d")
    factor = f.args.get("factor", "TechnicalFactor")
    if "tab-factor" == active_tab:
        return factor_app.factor_layout(trader, provider, entity, entity_type=entityType, level=level, factor=factor)


zvt_app.layout = serve_layout
# zvt_app.layout = debug_layout


def main():
    init_plugins()
    # zvt_app.run_server(debug=True)
    zvt_app.run_server(host="0.0.0.0")


if __name__ == "__main__":
    main()
