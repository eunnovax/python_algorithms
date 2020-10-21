import heapq, math

class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance

def closest_k_stars(stars, k): # O(nlogk) time, O(k) space
    max_heap = []
    result = []
    for star in stars:
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k+1:
            heapq.heappop(max_heap)
    return [s[1].distance for s in heapq.nlargest(k, max_heap)]

s1 = Star(1,2,1)
s2 = Star(1,1,1)
s3 = Star(3,3,3)
s4 = Star(4,4,4)
s5 = Star(5,5,5)
stars = [s1,s2,s3,s4,s5]
print(closest_k_stars(stars, 3))