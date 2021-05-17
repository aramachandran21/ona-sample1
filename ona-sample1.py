import csv
from operator import itemgetter
import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
with open('nodelist2.csv', 'r') as nodecsv: # Open the file
 nodereader = csv.reader(nodecsv) # Read the csv
 # Retrieve the data (using Python list comprhension and list slicing to remove the header row, see footnote 3)
 nodes = [n for n in nodereader][1:]
node_names = [n[0] for n in nodes] # Get a list of only the node names
with open('edgelist.csv', 'r') as edgecsv: # Open the file
 edgereader = csv.reader(edgecsv) # Read the csv
 edges = [tuple(e) for e in edgereader][1:] # Retrieve the data
 
G = nx.Graph()
G.add_nodes_from(node_names)
G.add_edges_from(edges)
pos=nx.spring_layout(G,k=0.75,iterations=20)
 # Loop through every node, in our data "n" will be the name of the person
points = ['Margaret Fell', 'George Whitehead']
path = nx.all_shortest_paths(G, source=points[0], target=points[1])
paths = nx.all_simple_paths(G, source=points[0], target=points[1],cutoff=5)
lst = list(path)
lst1 = list(paths)
#colors=list(mcolors.CSS4_COLORS)
colors=list(mcolors.BASE_COLORS)
print(lst)
z = [tuple(y) for y in lst]
z1 = [tuple(y1) for y1 in lst1]
z2 = set(z1) - set(z)
z3 = [list(x) for x in z2]
for e in G.edges():
 G[e[0]][e[1]]['color'] = 'lightseagreen'
 G[e[0]][e[1]]['alp'] = 0.3
j=1 
i=10
# Set color of edges of the shortest path to green
for list1 in z3:
 print(list1)
 for i in range(len(list1)-1):
 G[list1[i]][list1[i+1]]['color'] = 'orange'
 G[list1[i]][list1[i+1]]['alp'] = i
 i+=10
for list1 in lst:
 
 for i in range(len(list1)-1):
 G[list1[i]][list1[i+1]]['color'] = colors[j]
 G[list1[i]][list1[i+1]]['alp'] = 5
j=j+1
# Store in a list to use for drawing
edge_color_list = [ G[e[0]][e[1]]['color'] for e in G.edges() ]
alph = [ G[e[0]][e[1]]['alp'] for e in G.edges() ]
# print(edge_color_list)
node_colors = ["lightseagreen" if n in points else "red" for n in G.nodes()]
#print(G.edges())
labels = {}
for node in G.nodes():
labels[node] = node
# path_edges = zip(path,path[1:])
# path_edges = set(path_edges)
nx.draw_networkx_nodes(G, pos=pos,label=labels,font_size=15,node_color=node_colors)
nx.draw_networkx_edges(G, pos=pos,edge_color = edge_color_list,width=alph)
nx.draw_networkx_labels(G, pos=pos, font_size=9)
