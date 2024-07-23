import g_func
import cn
import ra
import aa
import compare_cn_ra_aa

def check_edge_in_list(e:tuple,e_list:list[tuple]) -> bool :
    if e == tuple() :
        return False
    
    a : int = e[0]
    b : int = e[1]

    if e in e_list : 
        return True
    elif (b,a) in e_list :
        return True
    else : 
        return False

def eval_best_ones(n_list:list[int],e_list_given:list[tuple],e_list_ex:list[tuple]) -> None :
    candidates : list[tuple] = compare_cn_ra_aa.best_ones(n_list,e_list_given)
    cn : tuple = candidates[0]
    ra : tuple = candidates[1]
    aa : tuple = candidates[2]

    if check_edge_in_list(cn,e_list_ex) :
        print(cn, "predicted by CN")
    else :
        print(cn, "incorrect prediction by CN")
    if check_edge_in_list(ra,e_list_ex) :
        print(ra, "predicted by RA")
    else :
        print(ra, "incorrect prediction by RA")
    if check_edge_in_list(aa,e_list_ex) :
        print(aa, "predicted by AA")
    else : 
        print(aa, "incorrect prediction by AA")

def eval_cn(n_list:list[int],e_list_given:list[tuple],e_list_ex:list[tuple]) -> None :
    candidates : list[tuple] = g_func.exclu_edges(e_list_given,cn.best_cn(n_list,e_list_given))
    
    for x in candidates :
        if check_edge_in_list(x,e_list_ex) :
            print(x,"O")
        else :
            print(x,"X")

def eval_ra(n_list:list[int],e_list_given:list[tuple],e_list_ex:list[tuple]) -> None :
    candidates : list[tuple] = g_func.exclu_edges(e_list_given,ra.best_ra(n_list,e_list_given))

    for x in candidates :
        if check_edge_in_list(x,e_list_ex) :
            print(x,"O")
        else :
            print(x,"X")
        
def eval_aa(n_list:list[int],e_list_given:list[tuple],e_list_ex:list[tuple]) -> None :
    candidates : list[tuple] = g_func.exclu_edges(e_list_given,aa.best_aa(n_list,e_list_given))

    for x in candidates :
        if check_edge_in_list(x,e_list_ex) :
            print(x,"O")
        else :
            print(x,"X")

def eval_all(n_list:list[int],e_list_given:list[tuple],e_list_ex:list[tuple]) -> None :
    print("-- evaluate CN -- ")
    eval_cn(n_list,e_list_given,e_list_ex)
    print("\n-- evaluate RA --")
    eval_ra(n_list,e_list_given,e_list_ex)
    print("\n-- evaluate AA --")
    eval_aa(n_list,e_list_given,e_list_ex)


#TESTS
    
#graph 1
"""n_list : list[int] = [0,1,2,3,4,5,6,7,8,9]
e_list : list[tuple] = [(0,1),(0,2),(0,3),
                        (1,5),(1,9),
                        (2,7),(2,8),
                        (3,4),(3,7),
                        (4,5),(4,8),(4,9),
                        (5,6),(5,7),
                        (6,9),
                        (7,8)]               
e_list_given : list[tuple] = [(0,1),(0,3),
                              (1,9),
                              (2,7),(2,8),
                              (3,4),(3,7),
                              (4,5),
                              (5,6),(5,7),
                              (7,8)]
e_list_ex : list[tuple] = [(0,2),(1,5),(4,8),(4,9),(6,9)]
"""

#graph 2 + variations
n_list = [0,1,2,3,4,5,6,7,8,9]
e_list = [(0,7),(1,5),(2,5),(2,7),(3,5),(4,0),(4,9),(5,8),(5,6),(6,7),(7,0),(8,2),(9,7),(9,8),(9,0)]

#e_list_given = [(0,7),(1,5),(2,5),(2,7),(3,5),(4,0),(4,9),(5,8),(6,7),(7,0),(9,7),(9,8)]
#e_list_ex = [(9,0),(8,2),(5,6)]
#(9,0)

#e_list_given = [(0,7),(1,5),(2,5),(2,7),(3,5),(4,0),(5,6),(6,7),(7,0),(8,2),(9,0)]
#e_list_ex = [(4,9),(9,7),(9,8),(5,8)]
#(9,4)

#e_list_given = [(0,7),(1,5),(2,5),(2,7),(3,5),(4,0),(5,6),(6,7),(7,0),(8,2),(9,0),(9,8)]
#e_list_ex = [(4,9),(9,7),(5,8)]
#(9,4)

#e_list_given = [(0,7),(1,5),(2,5),(2,7),(3,5),(4,0),(5,6),(5,8),(6,7),(7,0),(8,2),(9,0)]
#e_list_ex = [(4,9),(9,7),(9,8)]
#(9,4)

#e_list_given = [(0,7),(1,5),(2,5),(2,7),(3,5),(4,0),(5,6),(5,8),(7,0),(8,2),(9,0),(9,8)]
#e_list_ex = [(4,9),(9,7),(6,7)]
#(9,4)

#e_list_given = [(0,7),(1,5),(2,5),(3,5),(4,0),(5,8),(7,0),(8,2),(9,8),(4,9),(9,7),(6,7)]
#e_list_ex = [(9,0),(2,7),(5,6)]
#(9,0)

"""print("-- start --")
g_func.print_info(n_list,e_list)
print("\n-- evaluate best ones --")
eval_best_ones(n_list,e_list_given,e_list_ex)
print("\n-- evaluate all --")
eval_all(n_list,e_list_given,e_list_ex)
print("-- fin --")"""