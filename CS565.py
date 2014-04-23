import networkx as nx
import matplotlib.pyplot as plt

n = 120
s = 3
g = nx.powerlaw_cluster_graph(n, 5, 0.5)
r = g.node.keys()
h = nx.Graph()
supernodes = []

#node correspondence
for i in range(n/s):
	h.add_node(i) # supernode
	supernodes[i] = [r[0], r[0].neighobors[0], r[0].neighbors[1]]

	#TODO extend to for loop from s-1 to 0 
	r.remove(r[0].neighobors[1])
	r.remove(r[0].neighobors[0])
	r.remove(r[0])

for i in range(n/s):
	h.add_weighted_edges_from([()])
