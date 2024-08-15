import d_func
import g_func
import calc_n
import formula

yeast = d_func.file_set("Yeast.txt")
print(yeast)
ref = d_func.reference(yeast)
print(ref)
e = d_func.convert(ref,yeast)
n = g_func.get_nodes(e)
print(len(n))

SR = calc_n.cand(n,e,True,True,formula.pL3Np,formula.SR)
JC = calc_n.cand(n,e,True,True,formula.pL3Np,formula.JC)
print("len(SR) = ",len(SR))
print("len(JC) = ",len(JC))