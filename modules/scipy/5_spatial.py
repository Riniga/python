"""
Spatial data is a representation in geometric space
"""

import numpy as np
import math
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
from scipy.spatial import KDTree
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import cosine
from scipy.spatial.distance import hamming
import matplotlib.pyplot as plt



# Connect all points with triangles
def ConnectWithTriangles():
    points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1]
    ])
    simplices = Delaunay(points).simplices
    plt.triplot(points[:, 0], points[:, 1], simplices)
    plt.scatter(points[:, 0], points[:, 1], color='r')
    plt.show()

# Souround points with a hull
def SouroundingHull():
    points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1],
    [1, 2],
    [5, 0],
    [3, 1],
    [1, 2],
    [0, 2]
    ])
    hull = ConvexHull(points)
    hull_points = hull.simplices
    plt.scatter(points[:,0], points[:,1])
    for simplex in hull_points:
        plt.plot(points[simplex,0], points[simplex,1], 'k-')
    plt.show()

# Nearest point
def NearestPoint(x,y):
    points = np.array([[1, -1],
                       [2, 3],
                       [-1, 3],
                       [2, -3]])
    kdtree = KDTree(points)
    res = kdtree.query((x,y))
    print(res)
    plt.scatter(points[:,0], points[:,1])
    plt.show()


def AngleBetweenPointsDistance():
    p1 = (1, 0)
    p2 = (10, 2)
    res = euclidean(p1, p2)
    print (res)
    print("Distance straight line between p1 and p2: " + str(res) )
    res = cityblock(p1, p2)
    print("Distance moving up, down, right, left between p1 and p2: " +  str(res))
    res = cosine(p1, p2)
    print("Angle between p1 and p2: " +  str(res))
    print(math.acos(res))
    points = np.array([p1,p2])
    plt.scatter(points[:,0], points[:,1])
    plt.show()

def BinaryDistance():
    p1 = (True, False, True)
    p2 = (False, True, True)
    res = hamming(p1, p2)
    print(res)

def StringToBinary(binarystring):
    result = []
    for char in binarystring: 
        bitstring = bin(ord(char))[2:].rjust(8, '0')
        #print(char + "=" + bitstring)
        for bit in bitstring:
            if (bit=='0'): result.append(False)
            else: result.append(True)
    return result

def BinaryDistance(string1, string2):
        
    binary1= StringToBinary(string1)
    binary2= StringToBinary(string2)
    res = hamming(binary1, binary2)
    print(res)

#ConnectWithTriangles()
#SouroundingHull()
#NearestPoint(-0.5, 2)
#AngleBetweenPoints()
#BinaryDistance()
BinaryDistance("karolin","kerstin")
#BinaryDistance("a","z")
