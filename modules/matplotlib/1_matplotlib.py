import matplotlib
import matplotlib.pyplot as plt
import numpy as np
cols=3
rows=2

print(matplotlib.__version__)

plt.subplot(rows,cols,1)
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
zpoints = np.array([2, 3, 9, 12])
plt.plot(xpoints, ypoints)
plt.plot(xpoints, zpoints, marker='o', ls='-.',lw='2' , c='g', ms = 20, mec = 'r', mfc = 'b') # o * . x X + p s D d | _ ....
plt.title("Sports Watch Data", fontdict ={'family':'serif','color':'darkred','size':15}, loc ='left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(axis='y', color='y', linestyle ='--', linewidth =0.5)


plt.subplot(rows,cols,2)
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x, y, c=colors)
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')
plt.title("Scatter example")

plt.subplot(rows,cols,3)
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["green", "yellow", "red", "#ffbf00"]
myexplode = [0.2, 0, 0, 0]

plt.legend(title = "Four Fruits:")
plt.pie(y, labels = mylabels, startangle = 90, explode = myexplode,  shadow = True,colors = mycolors)

plt.subplot(rows,cols,4)
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()

plt.subplot(rows,cols,5)
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x,y,color = "purple", height =0.8)

plt.subplot(rows,cols,6)
x = np.random.normal(170, 10, 250)
plt.hist(x)

plt.suptitle("Plots for demonstration")
plt.rcParams['figure.figsize'] = [6, 4]
plt.show()
