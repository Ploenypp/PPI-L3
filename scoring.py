import math
from itertools import product
from collections import Counter

import pandas as pd

# calculate scores for every possible pair with give method
def scores(G, method, metric, ex=True) :
    nodes = sorted(list(G.nodes))
    res = dict()

    for i in range(len(nodes)) :
        j = i + 1
        while j < len(nodes) :
            if metric == None : res[(nodes[i],nodes[j])] = method(G,nodes[i],nodes[j])
            else : res[(nodes[i],nodes[j])] = method(G,nodes[i],nodes[j],metric,ex)
            j += 1

    return res 

# create dataframe 
def convert_df(scores) :
    pairs = scores.keys()
    values =scores.values()
    res = {'pairs':pairs, 'scores':values}
    return pd.DataFrame(res)

def score_candidates(G, candidate_edges, method, metric, ex=True) :
    res = dict() 

    for n1,n2 in candidate_edges :
        if metric == None : res[(n1,n2)] = method(G,n1,n2)
        else : res[(n1,n2)] = method(G,n1,n2,metric,ex)

    return res

def top_N_candidates(edges_scores,n) :
    ranked = dict(Counter(edges_scores).most_common())
    if n == all : return ranked
    res = dict()
    for edge, score in ranked.items() :
        if len(res) == n : return res
        res[edge] = score
