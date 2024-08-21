import g_func

# if going to use 1 specific file for pL3N and pL3Np calc, then remove sip & non_adj_crit (always true)

def scores_indiv(nodes:list[int],edges:set[tuple],x:int,sip:bool,non_adj_crit:bool,method,sm) -> list[float] :
    res = [0] * nodes.index(x)
    #print(x," : ",end="")
    for n in nodes[nodes.index(x):] :
        #print(n," ",end="")
        if tuple((x,n)) not in edges and tuple((n,x)) not in edges :
            if sip == False and n == x :
                res.append(0)
            else :
                if non_adj_crit :
                    if n not in g_func.N(edges,x) :
                        res.append(method(edges,x,n,sm))
                    else :
                        res.append(0)
                else :
                    res.append(method(edges,x,n,sm))
        else :
            res.append(0)
    #print("\n")
    return res

def all_scores(nodes:list[int],edges:set[tuple],sip:bool,non_adj_crit:bool,method,sm) -> list[list[float]] :
    return [scores_indiv(nodes,edges,n,sip,non_adj_crit,method,sm) for n in nodes]

def cand(nodes:list[int],edges:set[tuple],sip:bool,non_adj_crit:bool,method,sm) -> set[tuple] :
    aux = set()
    max_val = 0.0
    scores = all_scores(nodes,edges,sip,non_adj_crit,method,sm)

    for line in scores :
        if max_val < max(line) :
            max_val = max(line)
            print(max_val)
    print("found max_val")

    for i in range(len(scores)) :
        for j in range(i,len(scores)) :
            if i!=j and scores[i][j] == max_val :
                aux.add(tuple((i,j)))
                print(tuple((i,j)))
    print("found all cand")

    res = set()
    for (a,b) in aux :
        if (a,b) not in res and (b,a) not in res :
            res.add(tuple((a,b)))
            print("\t",tuple((a,b)))
    return res

def apply(nodes:list[int],edges:set[tuple],sip:bool,non_adj_crit:bool,method,sm) -> None :
    first = cand(nodes,edges,sip,non_adj_crit,method,sm)
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