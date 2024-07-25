import g_func

# (!) uses intersect_neighbors
# (!) uses degree
def ra_pair(n_list:list[int],e_list:list[tuple],a:int,b:int) -> float :
    intersect : set[tuple] = g_func.intersect_neighbors(n_list,e_list,a,b)
    sum : float = 0.0
    for x in intersect :
        aux = g_func.degree(n_list,e_list,x)
        if aux > 0 :
            sum = sum + 1/aux
    return sum

def ra_indiv(n_list:list[int],e_list:list[tuple],x:int) -> list[float] :
    res : list[float] = []

    for n in n_list :
        if x != n :
            res.append(ra_pair(n_list,e_list,x,n))
        else :
            res.append(0.00)
    return res

def ra_all(n_list:list[int],e_list:list[tuple]) -> list[list[float]] :
    res : list[list[float]] = []

    for n in n_list :
        aux : list[float] = ra_indiv(n_list,e_list,n)
        res.append(aux)
    return res

def best_ra_node(n_list:list[int],e_list:list[tuple]) -> list[tuple] :
    # proposes best edges for each node a (given edge(a,b))
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

def best_ra_overall(n_list:list[int],e_list:list[tuple]) -> list[tuple] :
    # proposes edges based on overall best score
    res : list[tuple] = []
    max_val : float = 0
    all_ra : list[list[float]] = ra_all(n_list,e_list)

    # calculate max(RA)
    for i in range(len(all_ra)) :
        if max(all_ra[i]) > max_val :
            max_val = max(all_ra[i])

    # filter out edges for score max_val 
    for i in range(len(all_ra)) :
        for j in range(len(all_ra)) :
            if g_func.check_edge(res,(i,max)) and all_ra[i][j] == max_val :
                res.append(tuple((i,j)))
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

def apply_RA(n_list:list[int],e_list:list[tuple],method) -> list[tuple] :
    # returns new edge list (including new edges)

    ra_list : list[tuple] = method(n_list,e_list)
    print("\t - proposed edges : ", ra_list)
    ra_list = g_func.exclu_edges(e_list,method(n_list,e_list))
    print("\t - new edges : ", ra_list)

    return e_list + ra_list

def compare_methods_RA(n_list:list[int],e_list:list[tuple]) -> None :
    print("-- original graph --")
    g_func.graph(n_list,e_list)

    print("-- RA scores --")
    print_ra_tab(n_list,e_list)

    print("best_ra_overall")
    bro : list[tuple] = apply_RA(n_list,e_list,best_ra_overall)
    print("best_ra_node")
    brn : list[tuple] = apply_RA(n_list,e_list,best_ra_node)

    print("best_ra_overall")
    g_func.graph(n_list,bro)
    print("best_ra_node")
    g_func.graph(n_list,brn)
