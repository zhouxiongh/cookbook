"""
你有一个字符串，想从左至右将其解析为一个令牌流。
"""

from collections import namedtuple 

def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

if __name__ == "__main__":
    text = 'foo = 23 + 42 * 10'
    import re
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'
    master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

    for tok in generate_tokens(master_pat, text):
        print(tok)

