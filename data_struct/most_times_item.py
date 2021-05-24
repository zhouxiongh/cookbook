from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the',
         'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes',
         "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes',
         "you're", 'under']
more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

if __name__ == '__main__':
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print('top_three: {}'.format(top_three))
    word_counts.update(more_words)
    top_five = word_counts.most_common(5)
    print('top_five: {}'.format(top_five))
    a = Counter(words)
    print('a: {}'.format(a))
    b = Counter(more_words)
    print('b: {}'.format(b))
    c = a + b
    print('a+b: {}'.format(c))
    d = a - b
    print('a-b: {}'.format(d))
    e = b - a
    print('b-a: {}'.format(e))
