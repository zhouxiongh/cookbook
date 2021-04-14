"""
你需要执行简单的时间转换，比如天到秒，小时到分钟等的转换。
"""

if __name__ == "__main__":
    from datetime import timedelta, datetime
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c.days)
    print(c.seconds)
    print(c.seconds / 3600)
    print(c.total_seconds() / 3600)

    a = datetime(2012, 9, 23)
    print(a + timedelta(days=10))
    b = datetime(2012, 12, 21)
    print((b - a).days)
    now = datetime.today()
    print(now)

    # 在计算的时候，需要注意的是 datetime 会自动处理闰年