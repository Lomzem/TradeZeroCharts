import plotly.graph_objects as go
import pandas as pd


def add_gray_area(fig, x_start, x_end, y_low, y_high):
    fig.add_shape(
        type='rect',
        x0=x_start,
        x1=x_end,
        y0=y_low,
        y1=y_high,
        fillcolor='gray',
        opacity=0.5,
        layer='below',
        line=dict(width=0)
    )


def add_trade_triangle(fig, time, price, bull_color, bear_color):
    fig.add_trace(go.Scatter(
        mode='markers',
        x=['10:30'],
        y=[4.0],
        marker_symbol='triangle-down',
        marker_size=15
    ))


def make_chart(df: pd.DataFrame, increasing_color='#26A69A', decreasing_color='#EF5350', bg_color='#131722') -> None:
    fig = go.Figure(data=[
        go.Candlestick(
            x=df.timestamp.dt.strftime('%H:%M'),
            open=df.open,
            high=df.high,
            low=df.low,
            close=df.close,
            increasing_line_color=increasing_color,
            decreasing_line_color=decreasing_color,
        )
    ])

    y_low = df.low.min() * 0.95
    y_high = df.high.max() * 1.05

    fig.update_layout(
        xaxis_rangeslider_visible=False,
        yaxis_range=[y_low, y_high],
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        plot_bgcolor=bg_color,
        width=1920,
        height=1080
    )

    first_candle = df.timestamp[0].strftime('%H:%M')
    final_candle = df.timestamp.iloc[-1].strftime('%H:%M')

    # Add Premarket Indicator
    add_gray_area(fig, first_candle, x_end='09:30', y_low=y_low, y_high=y_high)

    # Add Postmarket Indicator
    add_gray_area(fig, x_start='16:00', x_end=final_candle,
                  y_low=y_low, y_high=y_high)

    add_trade_triangle(fig, '10:30', 4.0, increasing_color, decreasing_color)

    fig.show()


make_chart(pd.read_parquet('./test_parquet.parquet'))
