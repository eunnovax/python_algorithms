import random, itertools

def online_random_sample(packets, k):
    # Stores the 1st k elements
    sample = list(itertools.islice(packets, k))
    print('initial sample',sample)
    rest = list(itertools.islice(packets, k, len(packets)))
    print('rest', rest)
    # Have read th 1st k elem-s
    packets_streamed = k
    for d in rest:
        print('d', d)
        packets_streamed += 1
        # Generate a random number in [0, packets_stream - 1], and if this number is in
        # [0, k-1] (packets streamed so far), we replace that element from the sample with d
        packetid_to_replace = random.randrange(packets_streamed)
        print('packetid_to_replace', packetid_to_replace)
        if packetid_to_replace < k:
            sample[packetid_to_replace] = d
            print('sample', sample)
    return sample

#Time: O(n), Space: O(k)
arr = [1,2,3,4,5,6,7]
size = 4

print(online_random_sample(arr, size))