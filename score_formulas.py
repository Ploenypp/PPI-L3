import math
from collections import Counter

import pandas as pd

# calculate scores for every possible pair with give method
def scores(G,method,metric,ex=True) :
    nodes = sorted(list(G.nodes))
    res = dict()

    for i in range(len(nodes)) :
        j = i + 1
        while j < len(nodes) :
            if metric == None : res[(nodes[i],nodes[j])] = method(G,nodes[i],nodes[j])
            else : res[(nodes[i],nodes[j])] = method(G,nodes[i],nodes[j],metric,ex)
            j += 1

    return dict(Counter(res).most_common())

# create dataframe 
def convert_df(scores) :
    pairs = scores.keys()
    values =scores.values()
    res = {'pairs':pairs, 'scores':values}
    return pd.DataFrame(res)

