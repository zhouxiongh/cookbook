

if __name__ == "__main__":
    # strip 方法用于删除开始或结尾的字符
    s = ' hello world'
    print(s)
    print(s.lstrip())
    print(s.rstrip())

    t = '-----hello====='
    print(t.lstrip('-'))
    print(t.strip('-='))