import pandas as pd
df = pd.read_csv('modules\\pandas\\data2.csv')

print(df.info())
new_df = df.dropna()

print(new_df.info())
#df.fillna(130, inplace=True)

mean = df["Calories"].mean()
median = df["Calories"].median()
mode = df["Calories"].mode()[0]

df["Calories"].fillna(mode, inplace = True)
df.dropna(subset=['Date'], inplace = True) #Remove a row with Date not set
df.loc[7, 'Duration'] = 45
df['Date'] = pd.to_datetime(df['Date'], format='mixed')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

for x in df.index:
  if df.loc[x, "Maxpulse"] > 174:
    df.drop(x, inplace = True)

df.drop_duplicates(inplace = True)

print(df.info())
print(df.to_string())

csv = df.to_csv('modules\\pandas\\data3.csv', index=False)
print(csv)



