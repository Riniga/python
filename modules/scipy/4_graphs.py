"""
Graphs are stored in cs graphs
Adjacency Matrix contains connections betwwen elements


"""
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix
from numpy import random
import networkx as nx
import matplotlib.pyplot as plt

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

network_graph = nx.Graph(arr)
#nx.draw_networkx(network_graph)
#plt.show()

print ("- Connected ---------")
connections = nx.connected_components(network_graph)
for connection in connections:
    print (connection)

csr = csr_matrix(arr)
print ("- Dijkstra ---------")
print(dijkstra(csr, return_predecessors=True, indices=0))
print ("- Floyd Warshall ---------")
print(floyd_warshall(csr, return_predecessors=True))
print ("- Depth first ---------")
print(depth_first_order(csr, 1))
print ("- Breadth first ---------")
print(breadth_first_order(csr, 1))