from operator import attrgetter


class User:
    def __init__(self, user_id, user_score):
        self.user_id = user_id
        self.user_score = user_score

    def __repr__(self):
        return 'User(id:{}, score:{})'.format(self.user_id, self.user_score)


def sort_notcompare():
    users = [User(23, 3), User(3, 2), User(99, 1)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))
    # attrgetter() 函数通常会运行的快点，并且还能同时允许多个字段进行比较
    print(sorted(users, key=attrgetter('user_score', 'user_id')))
    # 同样适用于像 min() 和 max() 之类的函数
    print(max(users, key=attrgetter('user_score')))
    print(min(users, key=attrgetter('user_score')))


if __name__ == '__main__':
    sort_notcompare()
