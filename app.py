import dash
import dash_core_components as dcc
import dash_html_components as html
from layout import html_layout


from youtubegraph import YT_graph



global yt_vid_comments
yt_vid_comments = []


app = dash.Dash(__name__)

server=app.server

app.index_string = html_layout

tabs_styles = {
    'height': '44px',

}
tab_style = {
    'border': '3px solid #111111',
    'padding': '6px',
    'fontWeight': 'bold',
    'background':'#111111'
}

tab_selected_style = {
    'borderTop': '3px solid #000000',
    'borderBottom': '3px solid #282828',
    'color': '#ffffff',
    'padding': '6px',
    'fontWeight': 'bold',
    'background':'#282828'

}






#LAYOUT OF THE MAIN DASH APP


app.layout = html.Div([
    dcc.Tabs(value='tab-0',children=
    [dcc.Tab(label='Home', value='tab-0', style=tab_style, selected_style=tab_selected_style, children=[
            html.P(""),
            html.H1("SentimentZION "),
            html.Div([html.H2("Know what the world thinks!"),
                    html.P("We at SentimentZION are focused to paint the true picture of the world for you. The information that is provided is mined from YouTube about your topic for a relevant timeframe. This data is presented in a visual format that provides higher readability and ease of consumption."),
                    html.H4("So what am I seeing?"),
                    html.H2("-- YouTube--  "),
                    html.P("The comments from the videos of the official channels of the company,"),
                    html.P("for instance, displaying an analysis of the videos from Uber's official YouTube channels !"),
                    # html.P("-- Twitter: around 1000 most relevant tweets!"),
                    # html.P("-- Reddit : 150 most relevant comments each from across 5 most active subreddits,  "),
                    # html.P("for instance, 150x5=750 comments !"),
                    html.H4("What is the significance?"),
                    html.P("Most social networks project the views of the most vocal but a minority of users on their platforms, however, the majority of the users' opinion is not taken into consideration. We plan on providing a non-biased overview by mining each comment from various social media sites which returns a score on a scale of -1 to 1, which signifies the sentiments of people where '-1' being most negative sentiment i.e. people are unsatisfied with it and '+1' being most positive sentiment i.e. people are satisfied."),
                    html.P("Note: This data is changing every second and hence the results take time to analyze and convert this data into a consumable format so a little Patience will be appreciated")
                    ])

        ]),
        dcc.Tab(label='YouTube', value='tab-1', style=tab_style, selected_style=tab_selected_style, children=[
            html.Div([
                #html.Div(html.H1(children="Team Zion")),
                html.P(""),
                html.H3("Enter the term you want to analyse"),
                html.Div([
                    dcc.Input(
                        id = "yquery-input",
                        placeholder = "Enter the query you want to search",
                        type = "text",
                        value = "Covid19",
                        style={"margin-right": "15px"}
                    ),
                   html.Button('Submit', id='ysubmit-val', n_clicks=0),
                   html.P(""),
                ]),
                html.Div(
                    dcc.Graph(id="y-graph1", config={'displayModeBar': False})
                    ),
                html.P(""),
                html.Div(
                    dcc.Graph(id="y-graph2",)
                    ),
                html.P(""),
                html.Div(
                    dcc.Graph(id="y-graph3",)
                    ),
                html.P(""),
                html.Div(
                    dcc.Graph(id="y-graph4",)
                    )

            ])
        ]),
    ])
])


#FUNCTION TO UPDATE THE GRAPHS ONPRESS OF SUBMIT BUTTON

@app.callback(
    [dash.dependencies.Output("y-graph1","figure"),
    dash.dependencies.Output("y-graph2","figure"),
    dash.dependencies.Output("y-graph3","figure"),
    dash.dependencies.Output("y-graph4","figure")],
    [dash.dependencies.Input('ysubmit-val', 'n_clicks')],
    [dash.dependencies.State("yquery-input","value")])
def update_figyt(n_clicks,input_value):
    figure = YT_graph(n_clicks,input_value)
    figure1 = figure[0]
    figure2 = figure[1]
    figure3 = figure[2]
    figure4 = figure[3]

    return figure1, figure2, figure3, figure4





if __name__ == "__main__":
    app.run_server(port=8989, debug = True)
