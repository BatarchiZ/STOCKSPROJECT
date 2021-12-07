from Project import jupyter_import as jp


def Quartile25(x):
    return x.quantile(0.25)
def Quartile75(x):
    return x.quantile(0.75)
def Interquartilerange(x):
    return x.quantile(0.75) - x.quantile(0.25)
#Functions to have a clean table (with caps)
def Mean(x):
    return x.mean()
def Median(x):
    return x.median()
def StDeviation(x):
    return x.std()

def task7(BVSTD, PERSTD):
    filtered_df_123 = jp.filtered_df.reset_index(drop=True)

    groups = filtered_df_123.groupby('Sector')
    filtered_df_123 = groups.apply(lambda x: x[
        x['Price_Book_Ratio'] >= Mean(x['Price_Book_Ratio'] - BVSTD * StDeviation(x['Price_Book_Ratio']))])

    filtered_df_123 = filtered_df_123.reset_index(drop=True)
    groups = filtered_df_123.groupby('Sector')
    filtered_df_123 = groups.apply(
        lambda x: x[
            x['Price_Book_Ratio'] <= Mean(x['Price_Book_Ratio'] + BVSTD * StDeviation(x['Price_Book_Ratio']))])
    filtered_df_1234 = filtered_df_123.reset_index(drop=True)

    groups = filtered_df_1234.groupby('Sector')
    filtered_df_1234 = groups.apply(lambda x: x[x['Price_Earnings_Ratio'] >= Mean(
        x['Price_Earnings_Ratio'] -PERSTD * StDeviation(x['Price_Earnings_Ratio']))])

    filtered_df_1234 = filtered_df_1234.reset_index(drop=True)
    groups = filtered_df_1234.groupby('Sector')
    filtered_df_RES = groups.apply(lambda x: x[x['Price_Earnings_Ratio'] <= Mean(
        x['Price_Earnings_Ratio'] + PERSTD * StDeviation(x['Price_Earnings_Ratio']))])
    filtered_df_RES = filtered_df_RES.reset_index(drop=True)
    return filtered_df_RES