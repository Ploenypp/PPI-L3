import g_func
import formula
import calc_n
# create edge set
def extract(line) :
    a = ""
    b = ""
    i = 0

    while line[i] != "," :
        a += line[i]
        i += 1
    i += 1

    while i < len(line) - 1 :
        b += line[i]
        i += 1

    return tuple((a,b))

def file_set(file) :
    f = open(file,"r")
    reader = f.readline()
    reader = f.readline()
    res = set()

    while len(reader) != 0 :
        res.add(extract(reader))
        reader = f.readline()

    return res

def reference(edges) :
    ref = dict()
    i = 1
    for (a,b) in edges :
        if a not in ref.keys() :
            ref.update({a:i})
            i += 1
        if b not in ref.keys() :
            ref.update({b:i})
            i += 1
    return ref 

def convert(ref,edges) :
    res = set()
    for (a,b) in edges :
        res.add(tuple((ref.get(a),ref.get(b))))
    return res

"""yeast = file_set("Yeast.txt")
print(yeast)
ref = reference(yeast)
print(ref)
e = convert(ref,yeast)
n = g_func.get_nodes(e)
print(len(n))

SR = calc_n.cand(n,e,True,True,formula.pL3Np,formula.SR)
JC = calc_n.cand(n,e,True,True,formula.pL3Np,formula.JC)
print("len(SR) = ",len(SR))
print("len(JC) = ",len(JC))"""