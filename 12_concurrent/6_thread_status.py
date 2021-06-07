"""
你需要保存正在运行线程的状态，这个状态对于其他的线程是不可见的。
"""

from socket import socket, AF_INET, SOCK_STREAM
import threading
from functools import partial

class LazyConnection:
    def __init__(self, address, famliy=AF_INET, type=SOCK_STREAM) -> None:
        self.address = address
        self.family = famliy
        self.type = type
        self.local = threading.local()
    
    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already connected')
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.local.sock.close()
        del self.local.sock

def test(conn):
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')

        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
    
    print('Got {} bytes'.format(len(resp)))

if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))

    t1 = threading.Thread(target=test, args=(conn,))
    t2 = threading.Thread(target=test, args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
