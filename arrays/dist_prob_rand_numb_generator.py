import random, itertools, bisect

def nonuniform_random_number(numbers, probabilities):
    #thenumber = landing in the intervals
    #[0, p1], [p1, p1+p2], [p1+p2, p1+p2+p3]
    list_of_sum_of_probabilities = list(itertools.accumulate(probabilities))
    interval_idx = bisect.bisect(list_of_sum_of_probabilities, random.random())
    return numbers[interval_idx]

prob = [.5,.3,.2,.1]
arr = [2,20,45,32]
for i in range(10):
    print(nonuniform_random_number(arr, prob))
