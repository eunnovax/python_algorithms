def boats_to_save(weights, limit):
    weights.sort()  # O(nlogn)

    liferafts, i, j = 0, 0, len(weights) - 1
    while i <= j:
        if weights[i] + weights[j] <= limit:
            i += 1
            j -= 1
        else:
            j -= 1
        liferafts += 1
    return liferafts

w = [3,7,9,10,55,0,3]
limit = 66
print(boats_to_save(w, limit))

# Time - O(n*logn)
# Space - O(1)
