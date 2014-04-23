import networkx as nx
import matplotlib.pyplot as plt

n = 120
s = 3
g = nx.powerlaw_cluster_graph(n, 5, 0.5)
r = g.nodes()
h = nx.Graph()
supernodes = []

#node correspondence
for i in range(n/s):
	h.add_node(i) # supernode
	remaining = [x for x in set(g.neighbors(r[0])) & set(r)]
	supernodes[i] = nx.Graph(g.subgraph( [r[0], remaining[0], remaining[1]] ))
	#supernodes[i] = nx.Graph(g.subgraph( [r[0]] + remaining[0:s-1] ))

	#TODO test later, note need to remove in order
	#for (j=s-1; j>0; j--):
	#	r.remove(r[0].neighbors[j])
	r.remove(r[0].neighobors[1])
	r.remove(r[0].neighobors[0])
	r.remove(r[0])

for i in range(n/s):
	h.add_weighted_edges_from([(i,j, ) for j in ])
