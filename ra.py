import g_func

def ra_pair(n_list:list[int],e_list:list[int],a:int,b:int) -> float :
    intersect : set[tuple] = g_func.intersect_neighbors(n_list,e_list,a,b)
    sum : float = 0.0
    for x in intersect :
        aux = g_func.degree(n_list,e_list,x)
        if aux > 0 :
            sum = sum + 1/aux
    return sum

def ra_indiv(n_list:list[int],e_list:list[int],x:int) -> list[float] :
    res : list[float] = []

    for n in n_list :
        if x != n :
            res.append(ra_pair(n_list,e_list,x,n))
        else :
            res.append(0.00)
    return res

def ra_all(n_list:list[int],e_list:list[int]) -> list[list[float]] :
    res : list[list[float]] = []

    for n in n_list :
        aux : list[float] = ra_indiv(n_list,e_list,n)
        res.append(aux)
    return res

def best_ra(n_list:list[int],e_list:list[int]) -> list[tuple] :
    res : list[tuple] = []
    max : int = -1
    ra : list[list[float]] = ra_all(n_list,e_list)

    for i in range(len(n_list)) :
        max = i
        for j in range(len(n_list)) :
            if ra[i][j] > ra[i][max] :
                max = j
        res.append(tuple((i,max)))
    return g_func.check_edge_list(res)

def print_ra_tab(n_list:list[int],e_list:list[tuple]) -> None :
    tab : list[list[float]] = ra_all(n_list,e_list)

    print("     ",end="")
    for i in range(len(n_list)) :
        print(i,"   ",end="")
    print("\n")
    print("    ",end="")
    for i in range(len(n_list)+2) :
        print("- - ",end="")
    print("\n")

    for i in range(len(n_list)) :
        print(i,"| ",end="")
        for j in range(len(tab[i])) :
            if tab[i][j] == 0 :
                print("    |",end="")
            else :
                print("%.2f|"% tab[i][j],end="")
        print("\n")

def print_ra_tab_modif(n_list:list[int],e_list:list[tuple]) -> None :
    tab : list[list[float]] = ra_all(n_list,e_list)

    print("     ",end="")
    for i in range(len(n_list)) :
        print(i,"   ",end="")
    print("\n")
    print("    ",end="")
    for i in range(len(n_list)+2) :
        print("- - ",end="")
    print("\n")

    for i in range(len(n_list)) :
        print(i,"| ",end="")
        for j in range(i) :
            print("     ",end="")
        for j in range(i, len(tab[i])) :
            if tab[i][j] == 0 :
                print("    |",end="")
            else :
                print("%.2f|"% tab[i][j],end="")
        print("\n")

def RA(n:int,x:int) -> None :
    n_list : list[int] = g_func.nodes(n)
    e_list : list[tuple] = g_func.edges(n_list)
    e_list = g_func.add_x_edges(n_list,e_list,x)
    g_func.print_info(n_list,e_list)
    g_func.graph(n_list,e_list)

    print("-- apply Resource Allocation --\n RA scores \n")
    #print_ra_tab(n_list,e_list)
    #print("simplified RA table\n")
    print_ra_tab_modif(n_list,e_list)
    
    ra_list : list[tuple] = best_ra(n_list,e_list)
    print("proposed edges : ", ra_list)
    a_list : list[tuple] = g_func.exclu_edges(e_list,ra_list)
    print("new edges : ", a_list)

    e_list = e_list + a_list
    g_func.print_info(n_list,e_list)
    g_func.graph(n_list,e_list)

    print("-- fin --")

#test
#print("-- start --")
#RA(10,2)