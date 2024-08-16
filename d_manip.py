import csv
import g_func
import d_func
import formula

e_file = d_func.file_set("Yeast.txt")
ref = d_func.reference(e_file)
e = d_func.convert(ref,e_file)
n = g_func.get_nodes(e)

num_n = (int)(len(n)/10)
new_n = []
i = 1
while i < num_n + 1 :
    new_n.append(i)
    i += 1

new_e = set()
for (a,b) in e :
    if a <= num_n and b <= num_n :
        new_e.add(tuple((a,b)))

data = [["n1","n2","score"]]
for i in new_n :
    for j in new_n :
        data.append([i,j,round(formula.pL3Np(new_e,i,j,formula.SR),2)])


with open("scores.csv","w",newline='') as csvfile :
    writer = csv.writer(csvfile,dialect='excel')
    writer.writerows(data)
