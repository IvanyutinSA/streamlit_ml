import pandas as pd


def remove_duplicates_and_nulls(df):
    df = pd.DataFrame()
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

