import math
import g_func

def CN(e_list:list[tuple],a:int,b:int) -> int :
    if a == b :
        return 0
    return len(g_func.intersect_neighbors(e_list,a,b))

def RA(e_list:list[tuple],a:int,b:int) -> float :
    intersect : set[tuple] = g_func.intersect_neighbors(e_list,a,b)
    sum : float = 0.0
    
    if a != b :
        for x in intersect :
            aux = g_func.degree(e_list,x)
            if aux > 0 :
                sum = sum + 1/aux
    return sum

def AA(e_list:list[tuple],a:int,b:int) -> float :
    intersect : set[tuple] = g_func.intersect_neighbors(e_list,a,b)
    sum : float = 0.0
    
    if a != b :
        for x in intersect :
            aux = g_func.degree(e_list,x)
            if aux > 1 :
                sum = sum + 1/(math.log(aux))
    return sum

def p1(e_list:list[tuple],a:int,b:int) -> int :
    U = set(g_func.neighbors(e_list,a)).intersection(set(g_func.NN(e_list,b)))
    V = set(g_func.neighbors(e_list,b)).intersection(set(g_func.NN(e_list,a)))
    score : int = 0

    for u in U :
        for v in V :
            if u in g_func.neighbors(e_list,v) :
                score += 1
    
    return score

def pL3N(e_list:list[tuple],a:int,b:int) -> float :
    U = set(g_func.neighbors(e_list,a)).intersection(set(NN(e_list,b)))
    V = set(g_func.neighbors(e_list,b)).intersection(set(NN(e_list,a)))
    score : float = 0.0

    for u in U :
        for v in V :
            if u in g_func.neighbors(e_list,v) :
                score += (float)(1/(math.sqrt(g_func.degree(e_list,u)*g_func.degree(e_list,v))))
    return score
