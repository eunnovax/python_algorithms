class Queue():
    def __init__(self):
        self._enq, self._deq = [], []

    def enqueue(self, x):
        self._enq.append(x)

    # When dequeue is called, e/t in _enq is reverse stacked in _deq IF _deq is empty
    # IF _deq is not empty, then whatever is in _deq is popped first
    def dequeue(self):
        if not self._deq:
            while self._enq:
                self._deq.append(self._enq.pop())

        if not self._deq: 
            raise IndexError('empty queue')
        return self._deq.pop()

q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(0)
q.dequeue()
print(q._enq, q._deq)
q.enqueue(30)
q.enqueue(4)
q.dequeue()
q.dequeue()
q.dequeue()
print(q._enq, q._deq)
