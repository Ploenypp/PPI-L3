import d_func
import g_func
import calc_n
import formula

yeast = d_func.file_set("Yeast.txt")
ref = d_func.reference(yeast)
e = d_func.convert(ref,yeast)
n = g_func.get_nodes(e)

print(len(n))
num_n = (int)(len(n)/2)
print(num_n)

new_n = []
for i in range(num_n) :
    new_n.append(i)
print(len(new_n))

new_e = set()
for (a,b) in e :
    if a <= num_n and b <= num_n :
        new_e.add(tuple((a,b)))
print(len(new_e))

#SR = calc_n.cand(new_n,new_e,True,True,formula.pL3Np,formula.SR)
JC = calc_n.cand(n,e,True,True,formula.pL3Np,formula.JC)
#print("len(SR) = ",len(SR))
#print(SR)
print("len(JC) = ",len(JC))
print(JC)