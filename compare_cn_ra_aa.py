import g_func
import cn
import ra
import aa

def compare_tab(n_list:list[int],e_list:list[tuple]) -> None :
    print("-- CN scores --\n")
    cn.print_cn_tab_modif(n_list,e_list)
    print("-- RA scores --\n")
    ra.print_ra_tab_modif(n_list,e_list)
    print("-- AA scores --\n")
    aa.print_aa_tab_modif(n_list,e_list)

def intersect_edges(e1:list[tuple],e2:list[tuple]) -> list[tuple] :
    res = [x for x in e1 for y in e2 if g_func.eq_edge(x,y)]
    return g_func.check_edge_list(res)

def compare_edges(n_list:list[int],e_list:list[tuple]) -> None :
    cn_list = cn.best_cn(n_list,e_list)
    ra_list = ra.best_ra(n_list,e_list)
    aa_list = aa.best_aa(n_list,e_list)

    print("-- proposed edges -- ")
    print("CN (", len(cn_list), ") : ", cn_list)
    print("RA (", len(ra_list), ") : ", ra_list)
    print("AA : (", len(aa_list), ") : ", aa_list)

    cn_e = g_func.exclu_edges(e_list,cn_list)
    ra_e = g_func.exclu_edges(e_list,ra_list)
    aa_e = g_func.exclu_edges(e_list,aa_list)

    print("\n-- OG edges excluded --")
    print("CN (", len(cn_e), ") : ", cn_e)
    print("RA (", len(ra_e), ") : ", ra_e)
    print("AA : (", len(aa_e), ") : ", aa_e)

    inter_cn_ra = intersect_edges(cn_e,ra_e)
    inter_ra_aa = intersect_edges(ra_e,aa_e)
    inter_cn_aa = intersect_edges(cn_e,aa_e)

    print("\n-- intersect edges --")
    print("CN intersect RA (", len(inter_cn_ra),") : ", inter_cn_ra)
    print("RA intersect AA (", len(inter_ra_aa),") : ", inter_ra_aa)
    print("CN intersect AA(", len(inter_cn_aa),") : ", inter_cn_aa)
    print("\t intersect all : ", intersect_edges(inter_cn_ra,inter_ra_aa))

    ex_cn_ra = g_func.exclu_edges(ra_e,cn_e)
    ex_ra_cn = g_func.exclu_edges(cn_e,ra_e)
    ex_cn_aa = g_func.exclu_edges(aa_e,cn_e)
    ex_aa_cn = g_func.exclu_edges(cn_e,aa_e)
    ex_ra_aa = g_func.exclu_edges(aa_e,ra_e)
    ex_aa_ra = g_func.exclu_edges(ra_e,aa_e)

    print("\n-- differ edges --")
    print("CN differs from RA (", len(ex_cn_ra), ") : ", ex_cn_ra)
    print("RA differs from CN (", len(ex_ra_cn), ") : ", ex_ra_cn)
    print("CN differs from AA (", len(ex_cn_aa), ") : ", ex_cn_aa)
    print("AA differs from CN (", len(ex_aa_cn), ") : ", ex_aa_cn)
    print("RA differs from AA (", len(ex_ra_aa), ") : ", ex_ra_aa)
    print("AA differs from RA (", len(ex_aa_ra), ") : ", ex_aa_ra)

def cn_best_one(n_list:list[int],e_list:list[tuple]) -> tuple :
    cn_tab = cn.cn_all(n_list,e_list)
    max : int = 0
    edge : tuple = tuple()
    for i in range(len(n_list)) :
        for j in range(len(n_list)) :
            if cn_tab[i][j] > max :
                edge = tuple((i,j))
                max = cn_tab[i][j]
    return tuple((edge,max))

def ra_best_one(n_list:list[int],e_list:list[tuple]) -> tuple :
    ra_tab = ra.ra_all(n_list,e_list)
    max : float = 0.00
    edge : tuple = tuple()
    for i in range(len(n_list)) :
        for j in range(len(n_list)) :
            if ra_tab[i][j] > max :
                edge = tuple((i,j))
                max = ra_tab[i][j]
    return tuple((edge,max))

def aa_best_one(n_list:list[int],e_list:list[tuple]) -> tuple :
    aa_tab = aa.aa_all(n_list,e_list)
    max : float = 0.00
    edge : tuple = tuple()
    for i in range(len(n_list)) :
        for j in range(len(n_list)) :
            if aa_tab[i][j] > max :
                edge = tuple((i,j))
                max = aa_tab[i][j]
    return tuple((edge,max))

def best_ones(n_list:list[int],e_list:list[tuple]) -> list[tuple] :
    cn_best = cn_best_one(n_list,e_list)
    ra_best = ra_best_one(n_list,e_list)
    aa_best = aa_best_one(n_list,e_list)

    ra_edge = ra_best[0]
    ra_score = ra_best[1]
    aa_edge = aa_best[0]
    aa_score = aa_best[1]

    print("\n -- predicted best option for each --")
    print("CN : ", cn_best)
    print("RA : ", ra_edge, ", %.2f " % ra_score, ")")
    print("AA : ", aa_edge, ", %.2f" % aa_score, ")")

    return [cn_best[0]] + [ra_edge] + [aa_edge]

def compare(n_list:list[int],e_list:list[tuple]) -> None :
    compare_tab(n_list,e_list)
    compare_edges(n_list,e_list)
    aux = best_ones(n_list,e_list)

#test
"""n_list = g_func.nodes(20)
e_list = g_func.edges(n_list)
e_list = g_func.add_x_edges(n_list,e_list,5)
g_func.print_info(n_list,e_list)

compare(n_list,e_list)
g_func.graph(n_list,e_list)"""