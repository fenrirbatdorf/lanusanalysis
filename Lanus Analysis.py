# %%
#import pandas, check for missing values
import pandas as pd
north = pd.read_csv('Northern.csv')
south = pd.read_csv('Southern.csv')
print(north.isna().sum())
print(south.isna().sum())

# %%
bins = []
sum_len = 0
for column in north:
    column_len = pd.unique(north[column].values)
    bins.append(column_len)
    sum_len += (len(column_len))
    print(sum_len-2)

# %%
bins = []
sum_len = 0
for column in south:
    column_len = pd.unique(south[column].values)
    bins.append(column_len)
    sum_len += (len(column_len))
    print(sum_len-2)

# %%



