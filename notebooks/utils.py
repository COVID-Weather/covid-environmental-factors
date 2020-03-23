import pandas as pd
import numpy as np
import os

def func(x, a, b, c):
    return a * np.exp(b * x) + c

def load_jhu_df():
    dir_path = "../data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/"
    daily = os.listdir(dir_path)

    li = []
    for day in daily:
        if ".csv" not in day: continue
        df_day = pd.read_csv(dir_path+day, index_col=None, header=0)
        df_day['date'] = day.split(".")[0]
        li.append(df_day)

    df = pd.concat(li, axis=0, ignore_index=True, sort=False)
    return df

def growth_period(df, region, period=14, threshold=100.):
    if ~((df.loc[region]['Confirmed'] >= threshold).any()):
        return None
    else:
        emerged = np.where(df.loc[region]['Confirmed'] >= threshold)[0][0]
        return df.loc[region][emerged:emerged+period]['Confirmed']