import g_func
import math
import method

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

def p1(e_list:list[tuple],a:int,b:int) -> int :
    U = set(g_func.neighbors(e_list,a)).intersection(set(NN(e_list,b)))
    V = set(g_func.neighbors(e_list,b)).intersection(set(NN(e_list,a)))
    score : int = 0

    for u in U :
        for v in V :
            if u in g_func.neighbors(e_list,v) :
                score += 1
    
    return score

def scores_indiv_non_adj(n_list:list[int],e_list:list[tuple],x:int,method) -> list[float] :
    res : list[float] = []

    for n in n_list :
            if g_func.check_edge(e_list,tuple((x,n))) :
                res.append(method(e_list,x,n))
            else :
                res.append(0)
    
    return res

def scores_non_adj(n_list:list[int],e_list:list[tuple],method) -> list[list[float]] :
    return [scores_indiv_non_adj(n_list,e_list,n,method) for n in n_list]

def best_cand_p1(n_list:list[int],e_list:list[tuple],method) -> list[tuple] :
    res : list[tuple] = []
    max_val : float = 0.0
    all_scores : list[list[float]] = scores_non_adj(n_list,e_list,method)

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
    new : list[tuple] = best_cand_p1(n_list,e_list,method)
    print("\t - proposed edges : ", new)
    new = g_func.exclu_edges(e_list,new)
    print("\t - new edges : ", new)

    return e_list + new

def pL3N(e_list:list[tuple],a:int,b:int) -> float :
    U = set(g_func.neighbors(e_list,a)).intersection(set(NN(e_list,b)))
    V = set(g_func.neighbors(e_list,b)).intersection(set(NN(e_list,a)))
    score : float = 0.0

    for u in U :
        for v in V :
            if u in g_func.neighbors(e_list,v) :
                score += (float)(1/(math.sqrt(g_func.degree(e_list,u)*g_func.degree(e_list,v))))
    return score

#test
"""n1_list = [0,1,2,3,4]
e1_list = [(0, 3), (1, 2), (2, 0), (3, 4), (4, 3), (1, 0), (2, 3)]
print(NN(e1_list,1))
print(NN(e1_list,3))

print(p1(e1_list,1,3))

score_tab = cn_ra_aa.scores_all(n1_list,e1_list,p1)
cn_ra_aa.print_scores(score_tab)"""
