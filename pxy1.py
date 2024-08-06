import g_func
import cn_ra_aa

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

def best_cand_p1(n_list:list[int],e_list:list[tuple],method) -> list[tuple] :
    res : list[tuple] = []
    max_val : float = 0.0
    all_scores : list[list[float]] = cn_ra_aa.scores_all(n_list,e_list,method)

    # calculate max_val
    for i in range(len(all_scores)) :
        for j in range(len(all_scores)) :
            if all_scores[i][j] > max_val and g_func.check_edge(e_list,tuple((i,j))) :
                max_val = all_scores[i][j]
    
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

#test
"""n1_list = [0,1,2,3,4]
e1_list = [(0, 3), (1, 2), (2, 0), (3, 4), (4, 3), (1, 0), (2, 3)]
print(NN(e1_list,1))
print(NN(e1_list,3))

print(p1(e1_list,1,3))

score_tab = cn_ra_aa.scores_all(n1_list,e1_list,p1)
cn_ra_aa.print_scores(score_tab)"""
