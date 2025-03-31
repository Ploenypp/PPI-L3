import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# create graph from an edge list
def graph(edges) :
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

def visualizeGraph(G) :
    pos = nx.spring_layout(G, seed=13)
    nx.draw(G, pos, with_labels = True, font_weight = 'bold')
    plt.show()

# return set of neighbors of given node :
def neighbor(G,n) :
    return set(G.neighbors(n))

# intersection of a's and b's neighbors
def intersectAB(G,a,b) :
    return neighbor(G,a).intersection(neighbor(G,b))

# neighbors of nodes in given list
def neighborsList(G,lst) : # in parent nodes
    return {n2 for n1 in lst for n2 in neighbor(G,n1)}

def s_neighborsList(G,lst) : # excluding parent nodes
    return {n2 for n1 in lst for n2 in neighbor(G,n1) if n2 not in lst}