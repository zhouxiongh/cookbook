""" 你想让你的对象支持上下文管理协议 (with 语句) 
为了让一个对象兼容 with 语句，你需要实现enter () 和exit () 方法
"""

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None

if __name__ == '__main__':
    from functools import partial
    conn = LazyConnection(('www.python.org', 80))
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)

    # 当出现 with语句的时候，对象的
    # enter () 方法被触发，它返回的值 (如果有的话) 会被赋值给
    # as 声明的变量。然后，with 语句块里面的代码开始执行。最后， exit () 方法被触
    # 发进行清理工作