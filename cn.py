import g_func

# > note : (func) intersect_neighbors = Common Neighbors between pairs

def cn_indiv(n_list:list[int],e_list:list[tuple],x:int) -> list[int] :
    res : list[int] = [] 
    for n in n_list :
        if n != x :
            res.append(len(g_func.intersect_neighbors(n_list,e_list,x,n)))
        else :
            res.append(0)
    return res

def cn_all(n_list:list[int],e_list:list[tuple]) -> list[list[int]] :
    res : list[list[int]] = []

    for n in n_list :
        aux = cn_indiv(n_list,e_list,n)
        res.append(aux)
    return res

def best_cn(n_list:list[int],e_list:list[tuple]) -> list[tuple] :
    res : list[tuple] = []
    max : int = 0
    all_cn : list[list[int]] = cn_all(n_list,e_list)

    for i in range(len(all_cn)) :
        max = 0
        for j in range(len(all_cn[i])) :
            if all_cn[i][j] > all_cn[i][max] :
                max = j
        if g_func.check_edge(res,(i,max)) :
            res.append(tuple((i,max)))
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

def print_cn_tab_modif(n_list:list[int],e_list:list[tuple]) -> None :
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
        for j in range(i) :
            print("   ",end="")
        for j in range(i,len(tab[i])) :
            print(tab[i][j]," ",end="")
        print("\n")

def CN(n:int,x:int) -> None :
    n_list : list[int] = g_func.nodes(n)
    e_list : list[tuple] = g_func.edges(n_list)
    e_list = g_func.add_x_edges(n_list,e_list,x)
    g_func.print_info(n_list,e_list)
    g_func.graph(n_list,e_list)

    print("-- apply Common Neighors --\n CN scores \n")
    #print_cn_tab(n_list,e_list)
    #print("simplified CN table\n")
    print_cn_tab_modif(n_list,e_list)

    cn_list : list[tuple] = best_cn(n_list,e_list)
    print("proposed edges : ", cn_list)
    a_list : list[tuple] = g_func.exclu_edges(e_list,cn_list)
    print("new edges : ", a_list)

    e_list = e_list + a_list
    g_func.print_info(n_list,e_list)
    g_func.graph(n_list,e_list)

    print("-- fin --")

#test
#print("-- start --")
#CN(5,2)