import random
import networkx as nx
import matplotlib.pyplot as plt
from typing import Final

NUMNODE : Final[int] = 5
3
""" > notes 
nodes : int
edges : tuple 
"""

# GRAPH GENERATION

def nodes(n:int) -> list[int] :
    return [i for i in range(n)]

# edges

def check_edge(e_list:list[tuple],e:tuple) -> bool :
    # true : add, false : retry/refuse
    a : int = e[0]
    b : int = e[1]
    if (a,b) in e_list :
        return False
    elif (b,a) in e_list : 
        return False
    elif a == b :
        return False
    return True

def edges(n_list:list[int]) -> list[tuple] :
    # initial set of edges : every node is connected to exactly one other node
    res : list[list[int]] = []
    n : int = len(n_list)

    for i in range(n) :
        x : int = random.randint(0,n-1)
        while i == x :
            x = random.randint(0,n-1)
        res.append(tuple((i,x)))
    return res

def add_x_edges(n_list:list[int],e_list:list[tuple],x:int) -> list[tuple] :
    n : int = len(n_list)
    a : int = random.randint(0,n-1)
    b : int = random.randint(0,n-1)

    while x > 0 :
        while check_edge(e_list,(a,b)) == False :
            a = random.randint(0,n-1)
            b = random.randint(0,n-1)
        e_list.append(tuple((a,b)))
        print("\t(",a,",",b,") added")
        x = x - 1
    return e_list

def graph(n_list:list[int],e_list:list[tuple]) -> None :
    G = nx.Graph()
    for x in n_list :
        G.add_node(x)
    for (a,b) in e_list :
        G.add_edge(a,b,color = 'b',weight = 4)
    nx.draw(G, with_labels = True, font_weight = 'bold')
    plt.show()
  
# CALCULATIONS + FUNCTIONS on GRAPHS

def neighbors(e_list:list[tuple],x:list) -> list[int] :
    aux : list[int] = []
    for (a,b) in e_list :
        if a == x :
            aux.append(b)
        elif b == x :
            aux.append(a)

    res : list[int] = []
    for i in aux :
        if i not in res :
            res.append(i)
    return res

def NN(e_list:list[tuple],x:int) -> list[int] :
    first = g_func.neighbors(e_list,x)
    second : list[int] = []

    for n in first :
        second += g_func.neighbors(e_list,n)
    
    res : list[int] = []
    for n in second :
        if n not in res :
            res.append(n)
    return res

# NOTICE : only considers 1st node in pair, check if considering 2nd affects other code
def edge_list_adj(n_list:list[int],e_list:list[tuple]) -> list[list[int]] :
    res : list[list[int]] = []
    for n in n_list :
        aux : list[int] = neighbors(e_list,n)
        res.append(aux)
    return res

# NOTICE : display of edges isn't a true adjacency list (no duplicates)
# (!) uses edge_list_adj
def print_info(n_list:list[int],e_list:list[tuple]) -> None :
    print("nodes : ", n_list)
    e_aux : list[list[int]] = edge_list_adj(n_list,e_list)
    print("edges\n")
    i : int = 0
    for e in e_aux :
        print(i,"| ",end="")
        for n in e :
            print(n," ",end="")
        print("\n")
        i = i + 1

# (!) uses neighbors
def degree(e_list:list[tuple],x:int) -> int :
    return len(neighbors(e_list,x))

# (!) uses neighbors
def intersect_neighbors(e_list:list[tuple],a:int,b:int) -> list[int] :
    a_n : list[int] = neighbors(e_list,a)
    b_n : list[int] = neighbors(e_list,b)

    if len(a_n) > len(b_n) :
        return [x for x in a_n if x in b_n]
    else :
        return [x for x in b_n if x in a_n]

def check_edge_list(e_list:list[tuple]) -> list[tuple] :
    res : list[tuple] = []
    for x in e_list :
        if check_edge(res,x) :
            res.append(x)
    return res

def exclu_edges(e1:list[tuple],e2:list[tuple]) -> list[tuple] :
    res = [x for x in e2 if check_edge(e1,x)]
    return check_edge_list(res)

# connectivity
def DFS(n_list:list[int],e_list:list[tuple],queue:list[int],visited:list[int]) -> list[int] :
    adjacent : list[int] = []
    for q in queue : 
        adjacent = adjacent + (neighbors(e_list,q))
    
    #print("queue:",queue)
    #print("visited:",visited)
    #print("neighbors:",neighbors)
    
    unvisited : list[int] = []
    for a in adjacent :
        if a not in visited and a not in queue and a not in unvisited :
            unvisited.append(a)
    #print("unvisited:",unvisited,"\n")

    res = visited + queue
    if unvisited == [] :
        return res
    return DFS(n_list,e_list,unvisited,res)

def sub_graphs(n_list:list[int],e_list:list[tuple],x:int) -> list[list[int]] :
    res : list[list[int]] = []
    connected = DFS(n_list,e_list,[x],[])
    res.append(connected)
    #print("-- connected:", connected)
    
    unconnected : list[int] = [n for n in n_list if n not in connected]
    #print("-- unconnected:", unconnected)
    if unconnected == [] :
        return res
    res = res + (sub_graphs(unconnected,e_list,unconnected[0]))
    return res

def connect(n_list:list[int],e_list:list[tuple]) -> list[tuple] :
    sub = sub_graphs(n_list,e_list,n_list[0])
    if len(sub) == 1 :
        print("graph already connected")
        return e_list
    else :
        for i in range(1,len(sub)) :
            e_list.append(tuple((sub[0][0],sub[i][0])))
            print("\t",tuple((sub[0][0],sub[i][0])),"added")
        return e_list
  
#generate random
"""n_list = nodes(NUMNODE)
e_list = edges(n_list)
e_list = add_x_edges(n_list,e_list,2)
print_info(n_list,e_list)
graph(n_list,e_list)"""

