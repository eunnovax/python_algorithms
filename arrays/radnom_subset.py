import random

def random_subset(n, k):
    hashmap = {}
    # generate random index b/w i and n-1
    for i in range(k):
        rand_idx = random.randrange(i,n)
        rand_idx_map = hashmap.get(rand_idx, rand_idx)
        i_map = hashmap.get(i,i)
        hashmap[rand_idx] = i_map
        hashmap[i] = rand_idx_map
    return [hashmap[i] for i in range(k)]

print(random_subset(100, 3))