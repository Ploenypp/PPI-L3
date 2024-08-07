import g_func

def scores_indiv(nodes:list[int],edges:set[tuple],x:int,non_adj_crit:bool,method) -> list[float] :
    res = []
    if non_adj_crit :
        for n in nodes :
            if n!= x and n not in g_func.N(edges,x) :
                res.append(method(edges,x,n))
            else :
                res.append(0)
        return res
    return [method(edges,x,n) for n in nodes]

def all_scores(nodes:list[int],edges:set[tuple],non_adj_crit:bool,method) -> list[list[float]] :
    return [scores_indiv(nodes,edges,n,non_adj_crit,method) for n in nodes]

def cand(nodes:list[int],edges:set[tuple],non_adj_crit:bool,method) -> set[tuple] :
    aux = set()
    max_val = 0.0
    scores = all_scores(nodes,edges,non_adj_crit,method)

    for i in range(len(scores)) :
        if max(scores[i]) > max_val :
            max_val = max(scores[i])

    for i in range(len(scores)) :
        for j in range(len(scores)) :
            if i!=j and scores[i][j] == max_val :
                aux.add(tuple((i,j)))
    
    res = set()
    for (a,b) in aux :
        if (a,b) not in res and (b,a) not in res :
            res.add(tuple((a,b)))
    return res

def apply(nodes:list[int],edges:set[tuple],non_adj_crit:bool,method) -> None :
    first = cand(nodes,edges,non_adj_crit,method)
    print("\t - proposed edges : ", first)
    
    new = set()
    for (a,b) in first :
        if (a,b) not in edges and (b,a) not in edges :
            new.add(tuple((a,b)))
    print("\t - new edges : ", new)
    
    return new.union(edges)

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