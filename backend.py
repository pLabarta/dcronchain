import requests
import plotly.graph_objs as go

# Toggle fig.show() to see intermediate charts

# GET JSON FROM GITHUB
json_url = 'https://gist.githubusercontent.com/pLabarta/27b1e395ed7d9a5edae5a70458d511b4/raw/36f63f21421bea2c99e2910fbea7058a9a26612a/Decred142-DayTicketUSDSum.json'
original_json = requests.get(json_url)

# GENERATE PLOTLY FIG FROM JSON
fig = go.Figure(original_json.json())
# SHOW ORIGINAL FIG ON BROWSER
#fig.show()

# CONFIGURE LAYOUT TEMPLATE
general_template = {
        "title_font_family": "Inconsolata, sans-serif",
        "legend_orientation": "h",
        "legend_x": 0,
        "legend_y": -0.3,
        "legend_font_family": "Inconsolata",
        "hoverlabel_font_family": "Inconsolata",
        # Y-AXIS
        "yaxis_title_font_family": "Inconsolata",
        "yaxis_tickfont_family": "Inconsolata",
        # X-AXIS
        "xaxis_title_font_family": "Inconsolata",
        "xaxis_tickfont_family": "Inconsolata",
        "xaxis_tickformat": "%b-%y",
        "font": {
            "color": "#091440"
        },
        # PLOT LAYOUT
        "paper_bgcolor": "white",
        "plot_bgcolor": "#ffffff",
        "annotations": {},
    }

# CONFIGURE SOME UNIQUE LAYOUT FOR THIS CHART
chart_template = {
        "title_font_family": "Inconsolata, sans-serif",
        "title_text": "Unique Chart Title",
    }
# Update with general template
fig.update_layout(general_template)
#fig.show()

#Update with unique template afterwards
fig.update_layout(chart_template)
#fig.show()

# WRITE NEW JSON FILE
fig.write_json('new.json')

# OR WRITE JSON AS JS SCRIPT
