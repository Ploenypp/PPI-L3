import g_func
import formula

# create edge set

# obj.split(",") instead of extract function
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

def record(max_val,edges) :
    f = open("rec_d_func.txt","a+")
    aux = "max_val = " + str(max_val) + " | " + str(edges) + "\n"
    f.write(aux)
    f.close()

def cand(edges) :
    nodes = g_func.get_nodes(edges)
    res = set()
    max_val = 0.0
    
    for i in nodes :
        for j in nodes:
            if tuple((i,j)) not in edges and i not in g_func.N(edges,j) :
                aux = round(formula.pL3Np(edges,i,j,formula.SR),2)
                if aux >= max_val :
                    res.clear()
                    res.add(tuple((i,j)))
                    if aux > max_val :
                        print("max_val = ",max_val)
                    max_val = aux
                    print("\t",tuple((i,j)))
    
    record(max_val,res)
    return res

