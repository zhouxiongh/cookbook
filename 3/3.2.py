"""
你需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现。
"""

if __name__ == "__main__":
    from decimal import Decimal
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a+b)
    print(a+b == Decimal('6.3'))

    # 总的来说， decimal 模块主要用在涉及到金融的领域