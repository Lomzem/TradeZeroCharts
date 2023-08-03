import datetime

import pandas as pd
import numpy as np

from polygon import RESTClient

from lomzem_env import *
from chart_maker import add_gray_area, add_trade_triangle
import plotly.graph_objects as go

class TradeZeroCharts:

    def __init__(self, api_key, multiplier: int = 1, time_unit: str = 'minute'):
        self.transaction_df = None
        self.api_key = api_key
        self.multiplier = multiplier
        self.time_unit = time_unit

    def df_from_csv(self, csv_path: str) -> None:
        self.transaction_df = pd.read_csv(csv_path, usecols=['T/D', 'Side', 'Symbol', 'Qty', 'Price', 'Exec Time'], parse_dates=[
                              'T/D', 'Exec Time'], dtype={'Side': 'category', 'Qty': np.uint16, 'Price': np.float32})
        self.transaction_df = self.transaction_df.rename(columns={'T/D': 'Date', 'Exec Time': 'Time'})
        self.transaction_df = self.transaction_df.groupby(['Date', 'Symbol'])

    def get_polygon_data(self, date: datetime.date, ticker: str) -> pd.DataFrame:
        client = RESTClient(api_key=self.api_key)
        aggs = client.get_aggs(
            ticker=ticker, multiplier=self.multiplier, timespan=self.time_unit, from_=date, to=date)
        return pd.DataFrame(aggs)
    
    def make_chart(self, df: pd.DataFrame, increasing_color: str = '#26A69A', decreasing_color='#EF5350', bg_color='#131722') -> None:
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

        if transactions_df is not None:
            for ticker in transactions_df
            add_trade_triangle(fig, '10:30', 4.0,
                            increasing_color, decreasing_color)

        fig.show()


client = TradeZeroCharts(api_key=api_key)
client.df_from_csv('file.csv')
client.make_chart()

TradeZeroCharts.make_chart

test = TradeZeroCharts(api_key=api_key)
# test.from_csv(trade_history_file)
# print((test.df))
# test.get_polygon_data()
print(test.make_chart())
# print(test.df.info())

client = TradeZeroCharts()
make_chart(TradeZeroCharts(api_key=api_key))

TradeZeroChart.make_chart()
