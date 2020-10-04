class QueueWithMax():  # O(1) dequeue, O(1) max, O(n) worst case enqueue times
    def __init__(self):
        self._entries = collections.deque()
        self._max_list = collections.deque()

    def enqueue(self, x):
        self._entries.append(x)
        # Eliminate smaller elements to get decreasing order in max_list
        while self._max_list and self._max_list[-1] < x:
            self._max_list.pop()
        self._max_list.append(x)

    def dequeue(self):
        if self._entries:
            result = self._entries.popleft()
            if result == self._max_list[0]:
                self._max_list.popleft()
            return result
        raise IndexError('empty queue')

    def max(self):
        if self._max_list:
            return self._max_list[0]
        raise IndexError('empty queue')
        
