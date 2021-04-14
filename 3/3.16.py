"""
你有一个安排在 2012 年 12 月 21 日早上 9:30 的电话会议，地点在芝加哥。而你的
朋友在印度的班加罗尔，那么他应该在当地时间几点参加这个会议呢？
"""

from datetime import datetime
from pytz import timezone


if __name__ == "__main__":
    # 对几乎所有涉及到时区的问题，你都应该使用 pytz 模块
    d = datetime(2012, 12, 21, 9, 30, 0)
    print(d)

    central = timezone('US/Central')
    loc_d = central.localize(d)
    print(loc_d)

    # Convert to Bangalore time
    bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
    print(bang_d)

    # 处理本地化日期的通常的策略先将所有日期转换为 UTC 时间，并用它来执行所有的中间存储和操作
    # 有可能 pytz 模块以及不再建议使用了，因为 PEP431提出了更先进的时区支持
    # PEP431 已经被 PEP615 取代