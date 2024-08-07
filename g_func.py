import networkx as nx
import matplotlib.pyplot as plt

def graph(nodes:list[int],edges:set[tuple]) -> None :
    G = nx.Graph()
    for n in nodes :
        G.add_node(n)
    for (a,b) in edges :
        G.add_edge(a,b,color = 'b',weight = 4)
    nx.draw(G, with_labels = True, font_weight = 'bold')
    plt.show()

def N(edges:set[tuple],x:int) -> set[int] :
    res = set()
    for (a,b) in edges :
        if a == x : 
            res.add(b)
        elif b == x :
            res.add(a)
    return res

def NN(edges:set[tuple],x:int) -> set[int] :
    first = N(edges,x)
    res = set()
    for n in first :
        res.union(N(edges,n))
    return res

def degree(edges:set[tuple],x:int) -> int :
    return len(N(edges,x))
