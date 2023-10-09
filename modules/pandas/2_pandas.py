import pandas as pd
print(pd.__version__)

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data, index=["day1","day2","day3"])
print(myvar)
print(myvar.loc["day2"])

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
print(myvar.loc[0])
print(myvar.loc[[0,1]])