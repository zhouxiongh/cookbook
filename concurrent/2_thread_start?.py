"""
你已经启动了一个线程，但是你想知道它是不是真的已经开始运行了
"""

from threading import Thread, Event
import time
import threading

def countdown(n):
    """
    int -> None
    from n count to 0
    """
    while n > 0:
        ptimer.wait_for_tick()
        print('T-minus', n)
        n -= 1

def countup(last):
    """
    int -> None
    from 0 count to last
    """
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1

# started_evt = Event()

# print('Launching countdown')
# t = Thread(target=countdown, args=(10, started_evt))
# t.start()

# # wait for the thread to start
# started_evt.wait()
# print('countdown is running')

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()
    
    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True

        t.start()
    

    def run(self):
        """
        Run the timer and notify waiting threads after each interval
        """
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()
    
    def wait_for_tick(self):
        """
        wait for the next tick of the timer
        """
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

ptimer = PeriodicTimer(5)
ptimer.start()

threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()