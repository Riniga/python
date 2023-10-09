import datetime
import random
import pandas as pd

df = pd.read_csv('modules\\pandas\\data.csv')
print(df)
print(df.to_string())
print(pd.options.display.max_rows) 
df = pd.read_json('modules\\pandas\\data.json')
print(df.head(10))


dates = []
for i in range(169):
  date=datetime.datetime(int(random.random()*4+2019), int(random.random()*12+1), int(random.random()*27+1))
  dates.append(date)

df["Dates"]= dates
print(df.head())

df.loc[len(df.index)] = [57, 108, 123,400.0, datetime.datetime(2022,9,13) ] 
print(df.tail())

df.sort_values(["Dates", "Pulse"], axis=0,
                 ascending=True, inplace=True)
print(df.tail())
print(df.info())