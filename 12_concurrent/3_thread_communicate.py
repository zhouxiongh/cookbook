"""
你的程序中有多个线程，你需要在这些线程之间安全地交换信息或数据
"""

from queue import Queue
from threading import Thread
import heapq
import threading

_sentinel = object()

class PriorityQueue:
    """
    Thread safe
    """
    def __init__(self) -> None:
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()
    
    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]
    
    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()

def producer(out_q):
    while True:
        # Produce some data
        out_q.put(data)
    
    # Put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)

def consumer(in_q):
    while True:
        data = in_q.get()

        if data is _sentinel:
            in_q.put(_sentinel)
            break
    # Process data
