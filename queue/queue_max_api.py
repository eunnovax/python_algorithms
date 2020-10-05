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
        
# More optimal soln Time O(1), Space - Best case O(1), Worst case O(n)
class Stack:
    class MaxWithCount:
        def __init__(self, max, count):
            self.max, self.count = max, count

    def __init__(self):
        self._element = []
        self._cached_max_with_count = []

    def empty(self):
        return len(self._element) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._cached_max_with_count[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        pop_element = self._element.pop()
        current_max = self._cached_max_with_count[-1].max
        if pop_element == current_max:
            self._cached_max_with_count[-1].count -= 1
            if self._cached_max_with_count[-1].count == 0:
                self._cached_max_with_count.pop()
        return pop_element

    def push(self, x):
        self._element.append(x)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(self.MaxWithCount(x, 1))
        else:
            current_max = self._cached_max_with_count[-1].max
            if x == current_max:
                self._cached_max_with_count[-1].count += 1
            elif x > current_max:
                self._cached_max_with_count.append(self.MaxWithCount(x, 1))

class QueueWithMaxConstant():  # O(1) for enqueue, dequeue, and max
    def __init__(self):
        self._enqueue = Stack()
        self._dequeue = Stack()

    def enqueue(self, x):
        self._enqueue.append(x)

    def dequeue(self):
        if self._dequeue.empty():
            while not self._enqueue.empty():
                self._dequeue.push(self._enqueue.pop())
        if not self._dequeue.empty():
            return self._dequeue.pop()
        raise IndexError('empty queue')
    
    def max(self):
        if not self._enqueue.empty():
            return self._enqueue.max() if self._dequeue.empty() else max(self._enqueue.max(), self._dequeue.max())
        if not self._dequeue.empty():
            return self._dequeue.max()
        raise IndexError('empty queue')


