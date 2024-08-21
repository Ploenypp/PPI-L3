import math
import g_func

def CN(edges:set[tuple],a:int,b:int) -> int :
    if a == b :
        return 0
    return len(g_func.N(edges,a).intersection(g_func.N(edges,b)))

def RA(edges:set[tuple],a:int,b:int) -> float :
    intersect = g_func.N(edges,a).intersection(g_func.N(edges,b))
    sum = 0.0

    if a!= b :
        for n in intersect :
            if g_func.degree(edges,n) > 0 :
                sum += 1/(g_func.degree(edges,n))
    return sum

def AA(edges:set[tuple],a:int,b:int) -> float :
    intersect = g_func.N(edges,a).intersection(g_func.N(edges,b))
    sum = 0.0

    if a != b :
        for n in intersect :
            if g_func.degree(edges,n) > 1 :
                sum += 1/(math.log(g_func.degree(edges,n)))
    return sum

def p1(edges:set[tuple],a:int,b:int) -> int :
    U = g_func.NintNN(edges,a,b)
    V = g_func.NintNN(edges,b,a)
    score = 0

    for u in U :
        for v in V :
            if u in g_func.N(edges,v) :
                score += 1
    return score

def pL3(edges:set[tuple],a:int,b:int) -> float :
    U = g_func.NintNN(edges,a,b)
    V = g_func.NintNN(edges,b,a)
    score = 0.0

    for u in U :
        for v in V :
            if u in g_func.N(edges,v) :
                score += (float)(1/(math.sqrt(g_func.degree(edges,u)*g_func.degree(edges,v))))
    return score

def SR(a:set,b:set) -> float :
    if len(a) == 0 :
        return 0.0
    return (float)(len(a.intersection(b))/len(a))

def JC(a:set,b:set) -> float :
    if len(a.union(b)) == 0 :
        return 0.0
    return (float)(len(a.intersection(b))/len(a.union(b)))

def pL3N(edges:set[tuple],x:int,y:int,sm) -> float :
    U = g_func.NintNN(edges,x,y)
    V = g_func.NintNN(edges,y,x)

    sum = 0.0
    for u in U :
        for v in V :
            if u in g_func.N(edges,v) :
                sum += sm(g_func.N(edges,y),g_func.N(edges,u)-{x}) * sm(g_func.N(edges,u)-{x},V) * sm(g_func.N(edges,v)-{y},U) * sm(g_func.N(edges,x),g_func.N(edges,v)-{y})
    
    return sm(g_func.N(edges,x),U) * sm(g_func.N(edges,y),V) * sum

def pL3Np(edges:set[tuple],x:int,y:int,sm) -> float :
    U = g_func.NintNN(edges,x,y)
    V = g_func.NintNN(edges,y,x)

    sum = 0.0

    for u in U :
        for v in V :
            if u in g_func.N(edges,v) :
                sum += sm(g_func.N(edges,y),g_func.N(edges,u)) * sm(g_func.N(edges,v),U) * sm(g_func.N(edges,x),g_func.N(edges,v)) * sm(g_func.N(edges,u),V)

    return sm(g_func.N(edges,x),U) * sm(g_func.N(edges,y),V) * sum