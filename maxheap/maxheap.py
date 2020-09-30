# public functions: push, peek, pop
# private functions: _swap, _floatUp, _bubbleDown

class MaxHeap():
    def __init__(self, items=[]):
        self.heap = []
        for i in items:
            self.heap.append(i)
            self._floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self._floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    
    def pop(self):
        if len(self.heap) > 2:
            self._swap(1, len(self.heap) - 1)
            maxValue = self.heap.pop()
            self._bubbleDown(1)
        elif len(self.heap) == 2:
            maxValue = self.heap.pop()
        else:
            maxValue = False
        return maxValue

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self._floatUp

    def _bubbleDown(self, index): #maxheapify
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._bubbleDown(largest)
    
m = MaxHeap([54, 5, 32])
m.push(13)
print(m.heap[0:len(m.heap)])
print(m.pop())
