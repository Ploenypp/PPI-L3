from math import *
from myfunc import *

# calculate Common Neighbors score for a pair of nodes
def CN(G,a,b) :
    if a == b : return 0
    return len(intersectAB(G,a,b))

# calculate Resource Allocation score for a pair of nodes
def RA(G,a,b) :
    if a == b : return 0
    return fsum([1/G.degree(n) for n in intersectAB(G,a,b) if 1/G.degree(n) > 0])

# calculate Adamic Adar Index for a pair of nodes
def AA(G,a,b) :
    if a == b : return 0 
    return fsum([1/log(G.degree(n)) for n in intersectAB(G,a,b) if 1/log(G.degree(n)) > 0])

# calculate the Simple Ratio of 2 sets
def SR(a,b) :
    if len(a) == 0 : return 0
    return len(a.intersection(b))/len(a)

# calculate the Jaccard coefficient of 2  sets
def JC(a,b) :
    if len(a.union(b)) == 0 : return 0
    return len(a.intersection(b))/len(a.union(b))

# True : excluding parent nodes
# False : including parent nodes

# calculate p(1) for a pair of nodes 
def p1(G,a,b,ex=True) :
    if a == b : return 0

    nA = neighbor(G,a)
    nB = neighbor(G,b)
    nnA, nnB = set(), set()

    if ex : # exclusively neighbors of distance 2
        nnA = s_neighborsList(G,nA) - {a}
        nnB = s_neighborsList(G,nB) - {b}
    else : # including parent nodes (not exclusively neighbors of distance 2)
        nnA = neighborsList(G,nA)
        nnB = neighborsList(G,nB)

    U = nA.intersection(nnB)
    V = nB.intersection(nnA)

    aux = 0
    for u in U :
        for v in V :
            if u in neighbor(G,v) : 
                aux += 1
    return aux

# calculate p(L3) for a pair of nodes
def pL3(G,a,b,ex=True) :
    if a == b : return 0

    nA = neighbor(G,a)
    nB = neighbor(G,b)
    nnA, nnB = set(), set()

    if ex : # exclusively neighbors of distance 2
        nnA = s_neighborsList(G,nA) - {a}
        nnB = s_neighborsList(G,nB) - {b}
    else : # including parent nodes (not exclusively neighbors of distance 2)
        nnA = neighborsList(G,nA)
        nnB = neighborsList(G,nB)

    U = nA.intersection(nnB)
    V = nB.intersection(nnA)

    sum = 0.0
    for u in U : 
        for v in V :
            aux = sqrt(G.degree(u)*G.degree(v))
            if aux > 0 : sum += 1/aux

    return sum

# calculate the pL3N score for a pair of nodes using a similarity metric
def pL3N(G,a,b,metric,ex=True) :
    if a == b : return 0

    nA = neighbor(G,a)
    nB = neighbor(G,b)
    nnA, nnB = set(), set()

    if ex : # exclusively neighbors of distance 2
        nnA = s_neighborsList(G,nA) - {a}
        nnB = s_neighborsList(G,nB) - {b}
    else : # including parent nodes (not exclusively neighbors of distance 2)
        nnA = neighborsList(G,nA)
        nnB = neighborsList(G,nB)

    U = nA.intersection(nnB)
    V = nB.intersection(nnA)

    aux = 0.0
    for u in U :
        for v in V :
            aux += metric(neighbor(G,u)-{a},V) * metric(neighbor(G,v)-{b},U) * metric(neighbor(G,a),neighbor(G,v)-{b}) * metric(neighbor(G,b),neighbor(G,u)-{a})

    return metric(nA,U) * metric(nB,V) * aux

# calculate the pL3N score for a pair of nodes using a similarity metric
def pL3Np(G,a,b,metric,ex=True) :
    if a == b : return 0

    nA = neighbor(G,a)
    nB = neighbor(G,b)
    nnA, nnB = set(), set()

    if ex : # exclusively neighbors of distance 2
        nnA = s_neighborsList(G,nA) - {a}
        nnB = s_neighborsList(G,nB) - {b}
    else : # including parent nodes (not exclusively neighbors of distance 2)
        nnA = neighborsList(G,nA)
        nnB = neighborsList(G,nB)

    U = nA.intersection(nnB)
    V = nB.intersection(nnA)

    aux = 0.0
    for u in U :
        for v in V :
            aux += metric(neighbor(G,u),V) * metric(neighbor(G,v),U) * metric(neighbor(G,a),neighbor(G,v)) * metric(neighbor(G,b),neighbor(G,u))
    return aux


