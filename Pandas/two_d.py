import pandas as pd

data = {
    "City" : ["Mumbai","Delhi","New York"],
    "Pin":[123,456,3432],
    "Country":["India","India","United States"]
}


# Row index are 0,1.. and cols are city pin country its like many series
df = pd.DataFrame(data)
# print(df.head(2))
# print(df.shape) # row x col
# print(df.describe())
# print(df[['City','Pin']])

# Slicing
# print(df[0:2]) # rows 0 to 1
# print(df.iloc[0:2,1:2]) # rows 0 to 1 and cols 1 only
# print(df.loc[0:1,'City':'Country']) # label based

print(df[(df['Country']=='India') & (df['City']=='Mumbai')])
print('\n')
print(df[df['City'].isin(['Mumbai','Delhi'])])

# Adding Data
df['Salary'] = [8999,23232,23232]
print(df,'\n')

# Modifying Data
df.loc[df['City']=='New York','Salary'] = 499999
print(df)

# dropping row/cols
df = df.drop('City',axis=1) # col drop
print(df)
df = df.drop(1,axis=0) # row drop
print(df)

df['Yearly Salary'] = df['Salary']*12
print(df)