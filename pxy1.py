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

#test
n1_list = [0,1,2,3,4]
e1_list = [(0, 3), (1, 2), (2, 0), (3, 4), (4, 3), (1, 0), (2, 3)]
print(NN(e1_list,1))
print(NN(e1_list,3))

print(p1(e1_list,1,3))

score_tab = cn_ra_aa.scores_all(n1_list,e1_list,p1)
cn_ra_aa.print_scores(score_tab)
