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
def N(G,node) :
    return set(G.neighbors(node))

def NList(G,lst,ex_parents = True) :
    if ex_parents :
        return {n2 for n1 in lst for n2 in N(G,n1) if n2 not in lst}
    return {n2 for n1 in lst for n2 in N(G,n1)} 