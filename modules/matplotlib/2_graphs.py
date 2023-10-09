from numpy import random
import networkx as nx
import matplotlib.pyplot as plt

network_graph = nx.Graph()
network_graph.add_edges_from(random.randint(20, size=(20, 2)))


print(network_graph.edges)

nx.draw_networkx(network_graph)
plt.show()