import pandas as pd


def transform(df):
    indicator = df['Indicator Name'].drop_duplicates()[0]
    df = df.set_index(['Country Name', 'Country Code']).drop(['Indicator Code', 'Unnamed: 64', 'Indicator Name'], axis=1).T
    df.index.name = 'Year'
    df = df.unstack()
    df.name = indicator
    df = pd.DataFrame(df)
    return df[~df[indicator].isnull()] 
