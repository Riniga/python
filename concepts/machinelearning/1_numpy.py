import json
import numpy
from scipy import stats
import matplotlib.pyplot as plt

file = open("concepts\\machinelearning\\data\\cars.json")
json_string = file.read()
cars = json.loads(json_string)
file.close()

speed = list()
age = list()
for car in cars:
  speed.append(car["Speed"])
  age.append(car["Age"])

print (speed)
print (numpy.mean(speed))
print (numpy.median(speed))
print (stats.mode(speed))
print (numpy.std(speed))
print (numpy.var(speed))
print(numpy.percentile(speed, 75))

# plt.hist(speed, 5)
# plt.show()

# x = numpy.random.uniform(0.0, 5.0, 250)
# x = numpy.random.normal(5.0, 1.0, 100000)
# plt.hist(x, 100)
# plt.show()

slope, intercept, r, p, std_err = stats.linregress(age, speed)
myfunc = lambda age : slope * age + intercept
mymodel = list(map(myfunc, age))

print (p);

# plt.scatter(age, speed)
# plt.plot(age, mymodel)
# plt.show()