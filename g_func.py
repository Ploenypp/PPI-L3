import networkx as nx
import matplotlib.pyplot as plt

def graph(nodes:list[int],edges:set[tuple]) -> None :
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    nx.draw(G, with_labels = True, font_weight = 'bold')
    plt.show()

def get_nodes(edges:set[tuple]) -> list[int] :
    G = nx.Graph()
    G.add_edges_from(edges)
    return sorted(G.nodes)

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
    for f in first :
        aux = N(edges,f)
        for n in aux :
            res.add(n)
    return res

def degree(edges:set[tuple],x:int) -> int :
    return len(N(edges,x))

def extract(line:str) -> tuple :
    aux = ""
    a = ""
    b = ""
    i = 0
    
    while line[i] != "," :
        aux += line[i]
        i += 1
    a = aux
    aux = ""
    i += 1
    while i < len(line) :
        aux += line[i]
        i += 1
    b = aux

    return tuple((int(a),int(b)))

def txt_set(file:str) -> set[tuple] :
    f = open(file,"r")
    reader = f.readline()
    reader = f.readline()
    res = set()

    while len(reader)!= 0 :
        res.add(extract(reader))
        reader = f.readline()
    
    f.close()
    return sorted(res)

#test 
#edges = txt_set("SyntheticPPI.txt")
#print(edges)

e = {(0,3),(1,2),(2,0),(3,4),(4,3),(1,0),(2,3)}
nodes = get_nodes(e)
print(sorted(nodes))