import pandas as pd
import numpy as np

from lomzem_env import *

class TradeZeroCharts:
    def __init__(self):
        self.df = None
    def from_csv(self, csv_path: str) -> None:
        self.df = pd.DataFrame(csv_path)

test = TradeZeroCharts()
test.from_csv('./TradeHistory20230802214519.csv')