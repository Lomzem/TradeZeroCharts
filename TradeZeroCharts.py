import datetime

import pandas as pd
import numpy as np

from lomzem_env import *

class TradeZeroCharts:
    def __init__(self):
        self.df = None
    def from_csv(self, csv_path: str) -> None:
        self.df = pd.read_csv(csv_path, usecols=['T/D', 'Side', 'Symbol', 'Qty', 'Price', 'Exec Time'], parse_dates=['T/D', 'Exec Time'], dtype={'Side': 'category', 'Qty': np.uint16, 'Price': np.float32})

test = TradeZeroCharts()
test.from_csv(trade_history_file)
print((test.df))
print(test.df.info())