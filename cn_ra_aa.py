import math
import g_func

def CN(n_list:list[int],e_list:list[tuple],a:int,b:int) -> int :
    if a == b :
        return 0
    return len(g_func.intersect_neighbors(n_list,e_list,a,b))

def RA(n_list:list[int],e_list:list[tuple],a:int,b:int) -> float :
    intersect : set[tuple] = g_func.intersect_neighbors(n_list,e_list,a,b)
    sum : float = 0.0
    
    if a != b :
        for x in intersect :
            aux = g_func.degree(n_list,e_list,x)
            if aux > 0 :
                sum = sum + 1/aux
    return sum

def AA(n_list:list[int],e_list:list[tuple],a:int,b:int) -> float :
    intersect : set[tuple] = g_func.intersect_neighbors(n_list,e_list,a,b)
    sum : float = 0.0
    
    if a != b :
        for x in intersect :
            aux = g_func.degree(n_list,e_list,x)
            if aux > 1 :
                sum = sum + 1/(math.log10(aux))
    return sum

def scores_indiv(n_list:list[int],e_list:list[tuple],x:int,method) -> list[float] :
    return [method(n_list,e_list,x,n) for n in n_list]

def scores_all(n_list:list[int],e_list:list[tuple],method) -> list[list[float]] :
    return [scores_indiv(n_list,e_list,n,method) for n in n_list]

def print_scores(tab:list[list[float]]) -> None :

    print("     ",end="")
    for i in range(len(tab)) :
        print(i,"   ",end="")
    print("\n")
    print("    ",end="")
    for i in range(len(tab)+2) :
        print("- - ",end="")
    print("\n")

    for i in range(len(tab)) :
        print(i,"| ",end="")
        for j in range(len(tab[i])) :
            if tab[i][j] == 0 :
                print("    |",end="")
            else :
                print("%.2f|"% tab[i][j],end="")
        print("\n")

def best_candidates(n_list:list[int],e_list:list[tuple],method) -> list[tuple] :
    res : list[tuple] = []
    max_val : float = 0.0
    all_scores : list[list[float]] = scores_all(n_list,e_list,method)

    # calculate max_val
    for i in range(len(all_scores)) :
        if max(all_scores[i]) > max_val :
            max_val = max(all_scores[i])
    
    # select those with max_val
    for i in range(len(all_scores)) :
        for j in range(len(all_scores)) :
            if g_func.check_edge(res,(i,max)) and all_scores[i][j] == max_val :
                res.append(tuple((i,j)))
    return g_func.check_edge_list(res)

def apply_method(n_list:list[int],e_list:list[tuple],method) -> None :
    new : list[tuple] = best_candidates(n_list,e_list,method)
    print("\t - proposed edges : ", new)
    new = g_func.exclu_edges(e_list,new)
    print("\t - new edges : ", new)

    return e_list + new