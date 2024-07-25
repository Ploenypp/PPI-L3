import math
import g_func

# (!) uses intersect_neighbors
# (!) uses degree
def aa_pair(n_list:list[int],e_list:list[tuple],a:int,b:int) -> float :
    intersect : set[tuple] = g_func.intersect_neighbors(n_list,e_list,a,b)
    sum : float = 0.0
    for x in intersect :
        aux = g_func.degree(n_list,e_list,x)
        if aux > 1 :
            sum = sum + 1/(math.log10(aux))
    return sum

def aa_indiv(n_list:list[int],e_list:list[tuple],x:int) -> list[float] :
    res : list[float] = []

    for n in n_list :
        if x != n :
            res.append(aa_pair(n_list,e_list,x,n))
        else :
            res.append(0.00)
    return res

def aa_all(n_list:list[int],e_list:list[tuple]) -> list[list[float]] :
    res : list[list[float]] = []

    for n in n_list :
        aux : list[float] = aa_indiv(n_list,e_list,n)
        res.append(aux)
    return res

def best_aa_node(n_list:list[int],e_list:list[tuple]) -> list[tuple] :
    res : list[tuple] = []
    max : int = -1
    aa : list[list[float]] = aa_all(n_list,e_list)

    for i in range(len(n_list)) :
        max = i
        for j in range(len(n_list)) :
            if aa[i][j] > aa[i][max] :
                max = j
        res.append(tuple((i,max)))
    return g_func.check_edge_list(res)

def best_aa_overall(n_list:list[int],e_list:list[tuple]) -> list[tuple] :
    # proposes edges based on overall best score
    res : list[tuple] = []
    max_val : float = 0
    all_aa : list[list[float]] = aa_all(n_list,e_list)

    # calculate max(AA)
    for i in range(len(all_aa)) :
        if max(all_aa[i]) > max_val :
            max_val = max(all_aa[i])

    # filter out edges for score max_val 
    for i in range(len(all_aa)) :
        for j in range(len(all_aa)) :
            if g_func.check_edge(res,(i,max)) and all_aa[i][j] == max_val :
                res.append(tuple((i,j)))
    return g_func.check_edge_list(res)

def print_aa_tab(n_list:list[int],e_list:list[tuple]) -> None :
    tab : list[list[float]] = aa_all(n_list,e_list)

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

def print_aa_tab_modif(n_list:list[int],e_list:list[tuple]) -> None :
    tab : list[list[float]] = aa_all(n_list,e_list)

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

def AA(n:int,x:int) -> None :
    n_list : list[int] = g_func.nodes(n)
    e_list : list[tuple] = g_func.edges(n_list)
    e_list = g_func.add_x_edges(n_list,e_list,x)
    g_func.print_info(n_list,e_list)
    g_func.graph(n_list,e_list)

    print("-- apply Adamic-Adar --\n AA scores \n")
    #print_aa_tab(n_list,e_list)
    #print("simplified AA table\n")
    print_aa_tab_modif(n_list,e_list)

    aa_list : list[tuple] = best_aa(n_list,e_list)
    print("proposed edges :", aa_list)
    a_list : list[tuple] = g_func.exclu_edges(e_list,aa_list)
    print("new edges : ", a_list)

    e_list = e_list + a_list
    g_func.print_info(n_list,e_list)
    g_func.graph(n_list,e_list)

    print("-- fin --")

def apply_AA(n_list:list[int],e_list:list[tuple],method) -> list[tuple] :
    # returns new edge list (including new edges)

    aa_list : list[tuple] = method(n_list,e_list)
    print("\t - proposed edges : ", aa_list)
    aa_list = g_func.exclu_edges(e_list,method(n_list,e_list))
    print("\t - new edges : ", aa_list)

    return e_list + aa_list

def compare_methods_AA(n_list:list[int],e_list:list[tuple]) -> None :
    print("-- original graph --")
    g_func.graph(n_list,e_list)

    print("-- RA scores --")
    print_aa_tab(n_list,e_list)

    print("best_ra_overall")
    bco : list[tuple] = apply_AA(n_list,e_list,best_aa_overall)
    print("best_ra_node")
    bcn : list[tuple] = apply_AA(n_list,e_list,best_aa_node)

    print("best_ra_overall")
    g_func.graph(n_list,bco)
    print("best_ra_node")
    g_func.graph(n_list,bcn)

#test
#print("-- start --")
#AA(10,2)