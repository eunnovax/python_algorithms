class Queue():
    scale_factor = 2

    def __init__(self, capacity):
        self._entries = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x):
        if self._num_queue_elements == len(self._entries): # Need to resize
            self._entries = (self._entries[self._head:] + self._entries[:self._head])
        # Resets head and tail
            self._head, self._tail = 0, self._num_queue_elements
            self._entries += [None] * (len(self._entries) * Queue.scale_factor - len(self._entries))
        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        print(self._tail)
        self._num_queue_elements += 1
    
    def dequeue(self):
        if not self._num_queue_elements:
            raise IndexError('empty queue')
        self._num_queue_elements -= 1
        ret = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return ret  
    
    def size(self):
        return self._num_queue_elements


que = Queue(4)
print(que.size())
for _ in range(5):
    que.enqueue(5)
print(que._entries)
que.dequeue()
print(que._head)
print(que._tail)
print(que._num_queue_elements)

