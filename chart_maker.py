import plotly.graph_objects as go
import pandas as pd

def make_chart(df: pd.DataFrame) -> None:
    fig = go.Figure(data=[
        go.Candlestick(
            x = df.timestamp.dt.strftime('%H:%M'),
            open = df.open,
            high = df.high,
            low = df.low,
            close = df.close,
        )
    ])
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()