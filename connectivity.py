import g_func

#g_func.neighbors() -> list of neighbors of node x

def re_neighbors(n_list:list[int],e_list:list[tuple],x:int) -> list[int] :
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

def DFS(n_list:list[int],e_list:list[tuple],queue:list[int],visited:list[int]) -> list[int] :
    neighbors : list[int] = []
    for q in queue : 
        neighbors = neighbors + (re_neighbors(n_list,e_list,q))
    
    #print("queue:",queue)
    #print("visited:",visited)
    #print("neighbors:",neighbors)
    
    unvisited : list[int] = []
    for n in neighbors :
        if n not in visited and n not in queue and n not in unvisited :
            unvisited.append(n)
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

#test
"""n_list = [0,1,2,3,4,5,6,7,8,9]
e_list = [(0,7),(1,5),(2,5),(2,7),(3,5),(4,0),(4,9),(5,8),(5,6),(6,7),(7,0),(8,2),(9,7),(9,8),(9,0)]

print("DFS result : ", DFS(n_list,e_list,[1],[]))
# 1 | 5 | 3 6 2 8 | 7 9 \ 0 4

print("DFS result : ", DFS(n_list,e_list,[0],[]))
# 0 | 7 9 4 | 6 2 8 | 5 | 3 1

print("DFS result : ", DFS(n_list,e_list,[2],[]))
# 2 | 5 7 8 | 6 9 0 3 1 | 4"""

"""n_list = n_list = [0,1,2,3,4,5,6,7,8,9]
e_list = [(0,7),(1,5),(2,5),(3,5),(4,0),(4,9),(5,6),(7,0),(9,7),(9,8),(9,0)]

#n_list = n_list = [0,1,2,3,4,5,6,7,8,9]
#e_list = [(1,5),(2,7),(3,5),(5,6),(8,2),(9,0)]

print(sub_graphs(n_list,e_list,5))
e_list = connect(n_list,e_list)
print("check")
print(sub_graphs(n_list,e_list,5))"""

#generate random
n_list = g_func.nodes(8)
e_list = g_func.edges(n_list)
e_list = connect(n_list,e_list)
e_list = g_func.add_x_edges(n_list,e_list,6)
g_func.print_info(n_list,e_list)
g_func.graph(n_list,e_list)
print(e_list)