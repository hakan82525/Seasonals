import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, dcc, html

# Generate random data
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=30, freq="D")
categories = ['A', 'B', 'C', 'D']

data = {
    'Date': np.tile(dates, 2),  # Repeat for 2 different series
    'Value': np.random.randint(10, 100, size=60),
    'Category': np.random.choice(categories, size=60)
}

df = pd.DataFrame(data)

# Summarize data for pie chart
pie_data = df['Category'].value_counts().reset_index()
pie_data.columns = ['Category', 'Count']

# Initialize the Dash app
app = Dash(__name__)
server = app.server  # Expose the server for Render.com

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Interactive Dashboard with Plotly Dash", style={'text-align': 'center'}),

    # Line chart
    html.Div([
        html.H3("Line Chart of Values Over Time"),
        dcc.Graph(
            figure=px.line(df, x='Date', y='Value', title="Line Chart")
        )
    ]),

    # Pie chart
    html.Div([
        html.H3("Pie Chart of Category Distribution"),
        dcc.Graph(
            figure=px.pie(pie_data, names='Category', values='Count', title="Category Distribution")
        )
    ]),

    # Scatter plot
    html.Div([
        html.H3("Scatter Plot of Value by Date"),
        dcc.Graph(
            figure=px.scatter(df, x='Date', y='Value', color='Category', title="Scatter Plot")
        )
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)  # Debug off for production
