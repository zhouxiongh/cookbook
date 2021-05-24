"""
你需要对多线程程序中的临界区加锁以避免竞争条件。
"""

import threading

class SharedCounter:
    """
    A counter object that can be shared by multiple threads.
    """
    _lock = threading.RLock()
    def __init__(self, initial_value = 0):
        self._value = initial_value
        # self._value_lock = threading.Lock()
    
    def incr(self, delta=1):
        """
        Increment the counter with locking
        """
        # with self._value_lock:
            # self._value += delta
        with SharedCounter._lock:
            self._value += delta

    def decr(self, delta=1):
        """
        Decrement the counter with locking
        """
        # with self._value_lock:
            # self._value -= delta
        with SharedCounter._lock:
            self._value -= delta
