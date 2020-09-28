def examine_buildings_for_sunset(sequence): # O(n) time, O(n) space always
    max_height = 0
    stack = [0]
    for item in reversed(sequence):
        if item > max_height: 
            stack.append(item)
        max_height = max(max_height, item)
    return [building_height for building_height in reversed(stack)] 

def examine_buildings_for_sunset_better(sequence): #O(n) time, O(n) worst case, O(1) best case space
    stack = []
    for item in sequence:
        while stack and item >= stack[-1]:
            stack.pop()
        stack.append(item)
    return stack

seq = [1,2,0,10,9,8,12,13,4,0]
print(examine_buildings_for_sunset(seq))
print(examine_buildings_for_sunset_better(seq))
        