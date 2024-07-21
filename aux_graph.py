import random

def gen_nodes() -> list[int] :
    n : int = random.randint(2,15)
    res : list[int] = [1,2]
    for i in range(3,n) :
        res = res + [i]
    return res

def gen_edges_nonconnexe(n_list:list[int]) -> list[tuple] :
    n : int = len(n_list)
    res : list[tuple] = []
    for i in range(0,n) :
        a : int = random.randint(1,n-1)
        b : int = random.randint(1,n-1)
        while b == a :
            b = random.randint(1,n-1)
        if tuple((a,b)) not in res :
            res.append(tuple((a,b,)))
    return res

def gen_edges_connexe(n_list:list[int]) -> list[tuple] :
    n : int = len(n_list)
    res : list[tuple] = []
    for i in range(1,n+1) :
        b : int = random.randint(1,n-1)
        while b ==i : 
            b = random.randint(1,n-1)
        res.append(tuple((i,b)))
    return res

def print_table(tab:list[list[int]]) -> None :
    x : int = 1
    print("    ",end="")
    while x < len(tab)+1 :
        print(x," ",end="")
        x = x + 1
    x = 0
    print("\n")
    print("    ",end="")
    while x < len(tab)+2 :
        print("- ",end="")
        x = x +1
    print("\n")

    x = 1
    for i in range (0,len(tab)) :
        print(x, "| ", end="")
        for j in range(0,len(tab[i])) :
            print(tab[i][j], " ", end="")
        print("\n")
        x = x + 1

def init_tab(n:int) -> list[list[int]] :
    return [[0] * n] * n
    
# tests
for i in range(10) :
    print(random.randint(0,9),',',random.randint(0,9))

