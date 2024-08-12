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
    U = g_func.N(edges,a).intersection(g_func.NN(edges,b))
    V = g_func.N(edges,b).intersection(g_func.NN(edges,a))
    score = 0

    for u in U :
        for v in V :
            if u in g_func.N(edges,v) :
                score += 1
    return score

def pL3(edges:set[tuple],a:int,b:int) -> float :
    U = g_func.N(edges,a).intersection(g_func.NN(edges,b))
    V = g_func.N(edges,b).intersection(g_func.NN(edges,a))
    score = 0.0

    for u in U :
        for v in V :
            if u in g_func.N(edges,v) :
                score += (float)(1/(math.sqrt(g_func.degree(edges,u)*g_func.degree(edges,v))))
    return score

def SR(a:set,b:set) -> float :
    return (float)(len(a.intersection(b))/len(a))

def JC(a:set,b:set) -> float :
    return (float)(len(a.intersection(b))/len(a.union(b)))

# DOUBLE CHECK SIM (CONTEXT?)
def Sim(edges:set[tuple],x:int,y:int,u:int,v:int) -> float :
    return JC(g_func.N(x),g_func.N(v)) + JC(g_func.N(y),g_func.N(u))

def pL3N(edges:set[tuple],x:int,y:int,sm) -> float :
    U = g_func.N(x).intersection(g_func.NN(y))
    V = g_func.N(y).intersection(g_func.NN(x))

    uV = 0.0
    vU = 0.0
    xv = 0.0
    yu = 0.0
    for u in U :
        for v in V :
            if u in g_func.N(v) :
                uV += sm(g_func.N(u)-{x},V)
                vU += sm(g_func.N(u)-{y},U)
                xv += sm(g_func.N(x),g_func.N(v)-{y})
                yu += sm(g_func.N(y),g_func.N(u)-{x})
    
    return sm(g_func.N(x),U) * sm(g_func.N(y),V) * uV * vU * xv * yu