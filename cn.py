import g_func

# > note : (func) intersect_neighbors = Common Neighbors between pairs

def cn_score_pair(n_list:list[int],e_list:list[tuple],a:int,b:int) -> int :
    if a == b :
        return 0
    return len(g_func.intersect_neighbors(n_list,e_list,a,b))

def cn_indiv(n_list:list[int],e_list:list[tuple],x:int) -> list[int] :
    # gives CN scores for a (in (a,v), v being various nodes)
    return [cn_score_pair(n_list,e_list,x,n) for n in n_list] 

def cn_all(n_list:list[int],e_list:list[tuple]) -> list[list[int]] :
    # gives CN scores for all node pairs
    return [cn_indiv(n_list,e_list,n) for n in n_list]

def best_cn(n_list:list[int],e_list:list[tuple]) -> list[tuple] :
    # proposes best edges for each node a (given edge (a,b))
    res : list[tuple] = []
    max : int = 0
    all_cn : list[list[int]] = cn_all(n_list,e_list)

    for i in range(len(all_cn)) :
        max = 0
        for j in range(len(all_cn)) :
            if all_cn[i][j] > all_cn[i][max] :
                max = j
        if g_func.check_edge(res,(i,max)) and all_cn[i][max] > 0 :
            res.append(tuple((i,max)))
    return g_func.check_edge_list(res)

def best_cn_overall(n_list:list[int],e_list:list[tuple]) -> list[tuple] :
    # proposes edges based on overall best score
    res : list[tuple] = []
    max_val : int = 0
    all_cn : list[list[int]] = cn_all(n_list,e_list)

    # calculate max(CN)
    for i in range(len(all_cn)) :
        if max(all_cn[i]) > max_val :
            max_val = max(all_cn[i])
    
    # filter out edges of score max_val
    for i in range(len(all_cn)) :
        for j in range(len(all_cn)) :
            if g_func.check_edge(res,(i,max)) and all_cn[i][j] == max_val :
                res.append(tuple((i,j)))
    return g_func.check_edge_list(res)

def print_cn_tab(n_list:list[int],e_list:list[tuple]) -> None :
    tab : list[list[int]] = cn_all(n_list,e_list)
    
    print("    ",end="")
    for i in range(len(n_list)) :
        print(i," ",end="")
    print("\n")
    print("    ",end="")
    for i in range(len(n_list)+2) :
        print("- ",end="")
    print("\n")

    for i in range(len(n_list)) :
        print(i,"| ",end="")
        for j in range(len(tab[i])) :
            print(tab[i][j]," ",end="")
        print("\n")

def CN(n:int,x:int) -> None :
    n_list : list[int] = g_func.nodes(n)
    e_list : list[tuple] = g_func.edges(n_list)
    e_list = g_func.add_x_edges(n_list,e_list,x)
    g_func.print_info(n_list,e_list)
    g_func.graph(n_list,e_list)

    print("-- apply Common Neighors --\n CN scores \n")
    print_cn_tab(n_list,e_list)
    #print("simplified CN table\n")
    #print_cn_tab_modif(n_list,e_list)

    cn_list : list[tuple] = best_cn(n_list,e_list)
    print("proposed edges : ", cn_list)
    a_list : list[tuple] = g_func.exclu_edges(e_list,cn_list)
    print("new edges : ", a_list)

    e_list = e_list + a_list
    g_func.print_info(n_list,e_list)
    g_func.graph(n_list,e_list)

    print("-- fin --")

def apply_CN(n_list:list[int],e_list:list[tuple],choice:function) -> None :
    print("-- original graph --")
    g_func.graph(n_list,e_list)
    
    print("-- CN scores --")
    print_cn_tab(n_list,e_list)

    cn_list : list[tuple] = choice(n_list,e_list)
    print("proposed edges : ", cn_list)
    cn_list = g_func.exclu_edges(e_list,choice(n_list,e_list))
    print("new edges : ", cn_list)
    

    e_list = e_list + cn_list
    print("-- new graph --")
    g_func.graph(n_list,e_list)
#test
#print("-- start --")
#CN(5,2)
n1_list = [0,1,2,3,4]
e1_list = [(0, 3), (1, 2), (2, 0), (3, 4), (4, 3), (1, 0), (2, 3)]
print(g_func.neighbors(n1_list,e1_list,4))
#print(cn_score_pair(n1_list,e1_list,0,4))
apply_CN(n1_list,e1_list)