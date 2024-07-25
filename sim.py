import random
import g_func
import test_cn_ra_aa

""" first made as an attempt to test if CN/RA/AA can predict removed edges 
    INCORRECT PREMISE 
        randomly generated graphs + randomly removed edges --> (assumption) no meaning to removal, therefore no meaning to prediction

    NOT MEANT FOR IMPLEMENTATION
    NOT UPDATED (calls to functions that no longer exist)
    NOT OPTIMIZED (may contain redundant code)
"""

def rem_x_edges(n_list:list[int],e_list:list[int],x:int) -> list[list[tuple]] :
    e_list_given : list[tuple] = e_list
    e_list_ex : list[tuple] = []
    res : list[list[tuple]] = []
    
    while x > 0 :
        aux_e : tuple = e_list[random.randint(0,len(e_list)-1)]
        aux_l : list[tuple] = [e for e in e_list_given if e != aux_e]
        if len(g_func.sub_graphs(n_list,aux_l,n_list[0])) == 1 :
            e_list_ex.append(aux_e)
            e_list_given = aux_l
            #print("- remaining : ",e_list_given)
            #print("- ex :",e_list_ex)
            x = x - 1
    res.append(e_list_given)
    res.append(e_list_ex)
    return res

#tests
n_list = g_func.nodes(25)
e_list = g_func.edges(n_list)
e_list = g_func.connect(n_list,e_list)
e_list = g_func.add_x_edges(n_list,e_list,5)
g_func.graph(n_list,e_list)


print("-- remove edges --")
rem = rem_x_edges(n_list,e_list,3)
e_list_given = rem[0]
e_list_ex = rem[1]
print("given edge list : ", e_list_given)
print("removed edges : ", e_list_ex)

print("-- check connectivity --")
e_list_given = g_func.connect(n_list,e_list_given)

print("\n-- start evaluation --")
#g_func.print_info(n_list,e_list)
print("\n-- evaluate best ones --")
test_cn_ra_aa.eval_best_ones(n_list,e_list_given,e_list_ex)
print("\n expected : ",e_list_ex)
print("\n-- evaluate all --")
test_cn_ra_aa.eval_all(n_list,e_list_given,e_list_ex)
print("-- fin --")