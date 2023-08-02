import datetime

import pandas as pd
import numpy as np

from polygon import RESTClient

from lomzem_env import *


class TradeZeroCharts:

    def __init__(self, api_key, multiplier: int = 1, time_unit: str = 'minute'):
        self.df = None
        self.ticker_df = None
        self.api_key = api_key
        self.multiplier = multiplier
        self.time_unit = time_unit

    def from_csv(self, csv_path: str) -> None:
        self.df = pd.read_csv(csv_path, usecols=['T/D', 'Side', 'Symbol', 'Qty', 'Price', 'Exec Time'], parse_dates=[
                              'T/D', 'Exec Time'], dtype={'Side': 'category', 'Qty': np.uint16, 'Price': np.float32})
        self.df = self.df.rename(columns={'T/D': 'Date', 'Exec Time': 'Time'})
        self.df = self.df.groupby(['Date', 'Symbol'])

    def get_polygon_data(self, date: datetime.date, ticker: str) -> pd.DataFrame:
        client = RESTClient(api_key=self.api_key)
        aggs = client.get_aggs(
            ticker=ticker, multiplier=self.multiplier, timespan=self.time_unit, from_=date, to=date)
        return pd.DataFrame(aggs)


test = TradeZeroCharts(api_key=api_key)
test.from_csv(trade_history_file)
# print((test.df))
test.get_polygon_data()
print(test.ticker_df)
# print(test.df.info())
