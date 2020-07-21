record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
SHARE = slice(20, 23)
PRICE = slice(31, 37)
cost1 = int(record[SHARE]) * float(record[PRICE])

if __name__ == '__main__':
    print("cost:{}, cost1:{}".format(cost, cost1))
