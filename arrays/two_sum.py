# Time - O(nlogn), Space - O(1)
# Actually, the solution is for "two subtraction" problem 
def two_sum(arr, diff):
    sorted_arr = sorted(arr)
    minReqSecPair, i = sorted_arr[0] + diff, 0
    secPair = -1
    while secPair < minReqSecPair:
        i += 1
        secPair = sorted_arr[i]
        print('second Pair', secPair)
    targetSecPair, j = sorted_arr[0] + diff, 0
    while targetSecPair < secPair:
        j +=1
        targetSecPair = sorted_arr[j] + diff
        print('targetSecPair', targetSecPair)
    return [sorted_arr[j], secPair] if targetSecPair == secPair else "No pair!"
    
l, d = [4,2,0,1,56,1,91,43], 86
print(two_sum(l, d))


        