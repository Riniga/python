import pandas as pd
df = pd.read_csv('modules\\pandas\\data4.csv')
c = df.corr()

print( c["Calories"]["Duration"])


