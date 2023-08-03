import datetime

import pandas as pd
import numpy as np

from polygon import RESTClient

from chart_maker import ChartMaker
from lomzem_env import *


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

    def make_chart(self):
        from chart_maker import ChartMaker
        chart_maker = ChartMaker()
        chart_maker.test_function()


test = TradeZeroCharts(api_key=api_key)
# test.from_csv(trade_history_file)
# print((test.df))
# test.get_polygon_data()
print(test.make_chart())
# print(test.df.info())