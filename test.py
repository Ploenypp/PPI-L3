import d_func
import g_func

e_file = d_func.file_set("Yeast.txt")
ref = d_func.reference(e_file)
e = d_func.convert(ref,e_file)
n = g_func.get_nodes(e)
print(n)

num_n = (int)(len(n)/10)
print(num_n)
new_n = []
i = 1
while i < num_n + 1 :
    new_n.append(i)
    i += 1
print(len(new_n))

new_e = set()
for (a,b) in e :
    if a <= num_n and b <= num_n :
        new_e.add(tuple((a,b)))
print(len(new_e))

candidates = d_func.cand(new_e)