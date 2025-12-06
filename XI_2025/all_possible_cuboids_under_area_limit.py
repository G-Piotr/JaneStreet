from collections import defaultdict

def generate_triples(max_area, n_max):
    """ n_max - max length over any axis """

    triples_by_P = defaultdict(list)
    
    for i in range(1, n_max + 1):
        for j in range(i, n_max + 1):
            for k in range(j, n_max + 1):
                P = 2 * (i*j + j*k + i*k)
                
                if P < max_area:
                    triples_by_P[P].append((i, j, k))
    
    return triples_by_P


result = generate_triples(max_area=140, n_max=140)
for P, triples in result.items():
    print(P, triples)

# In [13]: result[136]
# Out[13]: [(1, 2, 22), (2, 2, 16), (2, 4, 10), (2, 6, 7), (3, 4, 8)]
