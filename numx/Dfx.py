import pandas as pd
from typing import Dict
class Dfx:
    def __init__(self):
        pass

    def get_df(self, dct: Dict) -> pd.core.frame.DataFrame:
        df = pd.DataFrame(dct)
        #print(type(df))
        print(df.head(5))
        return df

    def get_df2(self, df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
        #print(type(df))
        df['sal2'] = df['sal'] * 1.3
        return df