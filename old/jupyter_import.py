# Initial Set-up
import io

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from Project import functions as fn

# Introduction
data = pd.read_csv(r'/Users/iskandersergazin/Desktop/financials.csv')
data = data.rename(columns={'Price/Earnings': 'Price_Earnings_Ratio', 'Earnings/Share': 'Earnings_Share_Ratio',
                            'Dividend Yield': 'Dividend_Yield', '52 Week Low': '52_Week_Low',
                            '52 Week High': '52_Week_High', 'Market Cap': 'Market_Cap',
                            'Price/Sales': 'Price_Sales_Ratio', 'Price/Book': 'Price_Book_Ratio'})
dp_intro = data.drop(['SEC Filings', 'EBITDA', '52_Week_Low', '52_Week_High', 'Symbol'], axis=1)

corr_intro = dp_intro.corr()
head_intro = dp_intro.head(10)
tail_intro = dp_intro.tail(20)

# Task 1
task1_table = dp_intro.agg(
    [fn.Mean, fn.StDeviation, fn.Median, fn.Quartile25, fn.Quartile75, fn.Interquartilerange]).round(2)

# Task 2
dp = dp_intro
bp1 = sns.boxplot(data=dp.Earnings_Share_Ratio, orient='h').set(
    xlabel='Ratio',
    ylabel='Companies',
    title='S&P 500 EPS Boxplot')
plt.savefig('Static/ESR_plot.jpeg')
figfile = io.BytesIO()
plt.savefig(figfile, format='jpeg')
plt.clf()

bp2 = sns.boxplot(data=dp.Price_Earnings_Ratio, orient='h').set(
    xlabel='Ratio',
    ylabel='Companies',
    title='S&P 500 PER Boxplot')
plt.savefig('Static/PER_plot.jpeg')
figfile = io.BytesIO()
plt.savefig(figfile, format='jpeg')
plt.clf()

bp3 = sns.boxplot(data=dp.Price_Sales_Ratio, orient='h').set(
    xlabel='Ratio',
    ylabel='Companies',
    title='S&P 500 PSR Boxplot')
plt.savefig('Static/PSR_plot.jpeg')
figfile = io.BytesIO()
plt.savefig(figfile, format='jpeg')
plt.clf()

bp4 = sns.boxplot(data=dp.Price_Book_Ratio, orient='h').set(
    xlabel='Ratio',
    ylabel='Companies',
    title='S&P 500 BV Boxplot')
plt.savefig('Static/BV_plot.jpeg')
figfile = io.BytesIO()
plt.savefig(figfile, format='jpeg')
plt.clf()
# plt.show()

'''Filtering'''
groups = dp.groupby('Sector')
# Removing Sector wise above PER outliers:
filtered_df = groups.apply(lambda x: x[
    x['Price_Earnings_Ratio'] <= fn.Quartile75(x['Price_Earnings_Ratio']) + 1.5 * fn.Interquartilerange(
        x['Price_Earnings_Ratio'])])
len(filtered_df)
# Removing sector wise below PER outliers:
filtered_df = filtered_df.reset_index(drop=True)

groups = filtered_df.groupby('Sector')
filtered_df = groups.apply(lambda x: x[
    x['Price_Earnings_Ratio'] >= fn.Quartile25(x['Price_Earnings_Ratio']) - 1.5 * fn.Interquartilerange(
        x['Price_Earnings_Ratio'])])

# Same operation for Price Book Ratio(BV):
filtered_df = filtered_df.reset_index(drop=True)
groups = filtered_df.groupby('Sector')
filtered_df = groups.apply(lambda x: x[
    x['Price_Book_Ratio'] >= fn.Quartile25(x['Price_Book_Ratio']) - 1.5 * fn.Interquartilerange(x['Price_Book_Ratio'])])

filtered_df = filtered_df.reset_index(drop=True)

groups = filtered_df.groupby('Sector')
filtered_df = groups.apply(lambda x: x[
    x['Price_Book_Ratio'] <= fn.Quartile75(x['Price_Book_Ratio']) + 1.5 * fn.Interquartilerange(x['Price_Book_Ratio'])])
filtered_df = filtered_df.reset_index(drop=True)
print(len(dp) - len(filtered_df))

# Task 1.1
filtered_dtf1 = filtered_df.agg(
    [fn.Mean, fn.StDeviation, fn.Median, fn.Quartile25, fn.Quartile75, fn.Interquartilerange]).round(2)

# Task2.1
table = filtered_df
table = pd.concat([table.Price_Book_Ratio, table.Price_Sales_Ratio], axis=0)
table.index = range(table.shape[0])
table = pd.DataFrame(table)
table['name'] = ''
table.loc[:table.shape[0] // 2, 'name'] = 'Price_Sales_Ratio'
table.loc[table.shape[0] // 2:, 'name'] = 'Price_Book_Ratio'
# table.loc[:table.shape[0]//2]
sns.boxplot(data=table, x=0, y='name', orient='h').set(
    xlabel='Ratio',
    ylabel='',
    title='S&P 500 PSR and PBR Boxplot')
plt.savefig('Static/PSR_PBR_plots.jpeg')
figfile = io.BytesIO()
plt.savefig(figfile, format='jpeg')
plt.clf()

table = filtered_df
table = pd.concat([table.Price_Earnings_Ratio, table.Earnings_Share_Ratio], axis=0)
table.index = range(table.shape[0])

table = pd.DataFrame(table)
table['name'] = ''
table.loc[:table.shape[0] // 2, 'name'] = 'Price_Earnings_Ratio'
table.loc[table.shape[0] // 2:, 'name'] = 'Earnings_Share_Ratio'
# table.loc[:table.shape[0]//2]
sns.boxplot(data=table, x=0, y='name', orient='h').set(
    xlabel='Ratio',
    ylabel='',
    title='S&P 500 PER and ESR Boxplot')
plt.savefig('Static/PER_ESR_plots.jpeg')
figfile = io.BytesIO()
plt.savefig(figfile, format='jpeg')
plt.clf()
# Task 3
'''Activate the cells below with caution /take a long time to execute/'''
# dp3 = dp[['Sector','Price_Earnings_Ratio']]
# dp3["Range"]=pd.cut(dp3.Price_Earnings_Ratio,range(int(dp3.Price_Earnings_Ratio.min()),int(dp3.Price_Earnings_Ratio.max()),2))
# dp3["Count"]=1
# dp4 = dp3.drop('Price_Earnings_Ratio',1).groupby(["Sector","Range"],
#                                                  as_index=False).sum()
# dp3 = dp[['Sector','Price_Earnings_Ratio']]
# dp3["Range"]=pd.cut(dp3.Price_Earnings_Ratio,range(int(dp3.Price_Earnings_Ratio.min()),int(dp3.Price_Earnings_Ratio.max()),2))
# dp3["Count"]=1
# dp4 = dp3.drop('Price_Earnings_Ratio',1).groupby(["Sector","Range"],as_index=False).count()
#
# sns.catplot(x = "Range",
#             y = "Count",
#             hue = "Sector",
#             data = dp4,
#             kind = "bar").fig.suptitle('PER Distribution by Sector (combined)')
#
# plt.savefig('Static/Task3_0_cat.jpeg')
# figfile = io.BytesIO()
# plt.savefig(figfile, format='jpeg')
# plt.clf()
#
# g = sns.catplot(y="Count", x="Range", col="Sector",
# data=dp4, saturation=.5,
# kind="bar", ci=None, aspect=.6).fig.suptitle('PER Distributions by Sector')
# plt.savefig('Static/Task3_0_cat_sect.jpeg')
# figfile = io.BytesIO()
# plt.savefig(figfile, format='jpeg')
# plt.clf()

# Task 3 Part 1.1:
sns.histplot(data=filtered_df, x='Price_Earnings_Ratio', hue='Sector').set_title('PER Histogram by Sector (combined)')
plt.savefig('Static/Task3_1_hist.jpeg')
figfile = io.BytesIO()
plt.savefig(figfile, format='jpeg')
plt.clf()

import random

colours = ['green', 'grey', 'blue', 'red', 'purple']

fig, axis = plt.subplots(1, 11, figsize=(30, 5))
counter = 0
for i in set(filtered_df.Sector):
    sns.histplot(ax=axis[counter], data=filtered_df[filtered_df.Sector == i],
                 x='Price_Earnings_Ratio', color=random.choice(colours), kde=True, legend=i)
    axis[counter].set_title(i)
    counter += 1
fig.suptitle('PER Distribution by Sector')
plt.savefig('Static/Task3_1_hist_sect.jpeg')
figfile = io.BytesIO()
plt.savefig(figfile, format='jpeg')
plt.clf()

# Plotting BV
colours = ['green', 'grey', 'blue', 'red', 'purple']
fig, axis = plt.subplots(1, 11, figsize=(30, 5))
counter = 0
for i in set(filtered_df.Sector):
    sns.histplot(ax=axis[counter], data=filtered_df[filtered_df.Sector == i],
                 x='Price_Book_Ratio', color=random.choice(colours), kde=True, legend=i)
    axis[counter].set_title(i)
    counter += 1
fig.suptitle('BV Distribution by Sector')
plt.savefig('Static/Task3_1_hist_BV_sect.jpeg')
figfile = io.BytesIO()
plt.savefig(figfile, format='jpeg')
plt.clf()

# Task 3 part 2:
q3p2 = data.Sector.value_counts()
q3p2 = data.Sector.value_counts()
dq3 = dp[['Sector', 'Market_Cap']]
dq3['intM_C'] = dq3.Market_Cap.fillna(dq3.Market_Cap.mean()).apply(lambda x: round(x))
dq3 = dq3.drop('Market_Cap', 1).groupby(['Sector'], as_index=True).sum()
dq3['ValueCounts'] = q3p2

dq3.plot.pie(y='intM_C', figsize=(10, 10)).set_title('S&P500 Market Capitalization Pie Chart (by sector)')
plt.savefig('Static/Task3_2_pie1.jpeg')
figfile = io.BytesIO()
plt.savefig(figfile, format='jpeg')
plt.clf()

dq3.plot.pie(y='ValueCounts', figsize=(10, 10)).set_title('S&P500 Number of Companies Pie Chart (by sector)')
plt.savefig('Static/Task3_2_pie2.jpeg')
figfile = io.BytesIO()
plt.savefig(figfile, format='jpeg')
plt.clf()

dq3['MeanPrice'] = filtered_df.groupby('Sector').Price.mean().apply(lambda x: round(x))
corr_3 = dq3.corr()

dq3['MeanPER'] = filtered_df.groupby('Sector').Price_Earnings_Ratio.mean().apply(lambda x: round(x))
dq3['MeanBV'] = filtered_df.groupby('Sector').Price_Book_Ratio.mean().apply(lambda x: round(x))
corr4 = dq3.corr()

sns.clustermap(dq3, cmap="mako", vmin=0, vmax=10).fig.suptitle('S&P 500 Cluster Map')
plt.savefig('Static/Task3_cluster.jpeg')
figfile = io.BytesIO()
plt.savefig(figfile, format='jpeg')
plt.clf()

# Task 6*
# Filtration for PER and BV:
filtered_df_123 = filtered_df.reset_index(drop=True)

groups = filtered_df_123.groupby('Sector')
filtered_df_123 = groups.apply(lambda x: x[
    x['Price_Book_Ratio'] >= fn.Mean(x['Price_Book_Ratio'] - 0.005 * fn.StDeviation(x['Price_Book_Ratio']))])

filtered_df_123 = filtered_df_123.reset_index(drop=True)
groups = filtered_df_123.groupby('Sector')
filtered_df_123 = groups.apply(
    lambda x: x[x['Price_Book_Ratio'] <= fn.Mean(x['Price_Book_Ratio'] + 0.01 * fn.StDeviation(x['Price_Book_Ratio']))])

filtered_df_1234 = filtered_df_123.reset_index(drop=True)

groups = filtered_df_1234.groupby('Sector')
filtered_df_1234 = groups.apply(lambda x: x[x['Price_Earnings_Ratio'] >= fn.Mean(
    x['Price_Earnings_Ratio'] - 0.005 * fn.StDeviation(x['Price_Earnings_Ratio']))])

filtered_df_1234 = filtered_df_1234.reset_index(drop=True)
groups = filtered_df_1234.groupby('Sector')
filtered_df_RES = groups.apply(lambda x: x[x['Price_Earnings_Ratio'] <= fn.Mean(
    x['Price_Earnings_Ratio'] + 0.005 * fn.StDeviation(x['Price_Earnings_Ratio']))])
filtered_df_RES = filtered_df_RES.reset_index(drop=True)
len(filtered_df_RES)

# Taking Samples
sample = filtered_df_RES.sample(n=10)[['Sector', 'Name', 'Price', 'Dividend_Yield']]

resu = pd.DataFrame()
resu['Name'] = ['Emerson Electric', 'McCormick&Co', 'Xilinx Inc', 'Texas Instruments', 'Boston Properties', 'Hologic',
                'Church&Dwight', 'Coca Cola', 'Expeditors International']
resu['Price03_11_21'] = [90.38, 87.01, 218.7, 193.58, 110.49, 73.77, 91.06, 53.07, 122.6]
# I have realised that the intial data for July 2020 is incorrect, thereby I am going to change the
# columns so that they represent the data of July 2020 as stated in the original information file.
resu['Price02_07_20'] = [61.65, 90.81, 99.14, 125.81, 91.55, 57.86, 78.29, 44.88, 77.15]
resu['PERCENT_CHANGE'] = ((resu['Price03_11_21'] - resu['Price02_07_20']) / resu['Price02_07_20']) * 100
resu
# Sample differs every time the code is run, this was the only way to produce a random sample.
# The drawback is that after this code is run, everything has to be done manually.

PC = fn.Mean(resu.PERCENT_CHANGE)
SP500_02_07_20 = 3130
SP500_03_11_21 = 4529
PCSP500 = (SP500_03_11_21 - SP500_02_07_20) / SP500_02_07_20 * 100
PCSP500

resu['Dividend'] = [2.8, 2.02, 2.09, 2.43, 2.77, 0, 1.83, 3.32, 1.35]
PT = PC + fn.Mean(resu.Dividend)
PT

resu2 = pd.DataFrame()
resu2['Price03_11_21'] = [90.38, 87.01, 218.7, 193.58, 110.49, 73.77, 91.06, 53.07, 122.6]
resu2['Price2017'] = [66.4, 101.36, 62.82, 97.66, 112.09, 38.8, 47.38, 43.10, 60.36]
resu2['PERCENT_CHANGE'] = ((resu2['Price03_11_21'] - resu2['Price2017']) / resu2['Price2017']) * 100
resu2

PC2 = fn.Mean(resu2.PERCENT_CHANGE)
PC2

SP500_2017_Jan = 2270
PCSP500_2 = (SP500_03_11_21 - SP500_2017_Jan) / SP500_2017_Jan * 100
SP500_2017_June = 2439
PCSP500_3 = (SP500_03_11_21 - SP500_2017_June) / SP500_2017_June * 100
SP500_2017_Dec = 2673
PCSP500_4 = (SP500_03_11_21 - SP500_2017_Dec) / SP500_2017_Dec * 100
PCSP500_2017 = pd.DataFrame([PCSP500_2, PCSP500_3, PCSP500_4])
finish = PCSP500_2017.mean()
