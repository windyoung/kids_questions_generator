import math


def test_math():
    number_limit = 27
    # root=math.sqrt(number_limit)
    # root=math.ceil(root)
    root = math.ceil(math.sqrt(number_limit))
    print(root)


def test_divid():
    divid1 = 5
    divid2 = 10
    res = divid1 // divid2
    res1 = divid1 % divid2
    print(res, res1)


def test_list():
    a = [{'＋': [6, 2]}, {'－': [6, 1]}, {'＋': [2, 1]}, {'＋': [4, 4]}, {'－': [8, 1]}, {'＋': [2, 0]}, {'－': [9, 0]}, {'－': [8, 0]}, {'＋': [4, 2]}, {'＋': [9, 0]}, {'－': [3, 3]}, {'－': [6, 2]}, {'＋': [3, 4]}, {'＋': [2, 0]}, {'－': [8, 2]}, {
        '－': [5, 5]}, {'＋': [0, 0]}, {'－': [6, 1]}, {'－': [5, 5]}, {'＋': [2, 7]}, {'－': [2, 1]}, {'－': [7, 3]}, {'－': [7, 2]}, {'－': [6, 2]}, {'－': [8, 1]}, {'－': [7, 1]}, {'－': [3, 3]}, {'＋': [5, 1]}, {'－': [9, 1]}, {'＋': [9, 0]}]
    b = tuple(a)
    print(b)


def test_dict():
    a = {'－': [10, 0]}
    a = {'－': [10, 0], '1': [10, 0]}
    print(list(a.keys()))

def test_minus():
    for a in range(20,-1,-1):
        print(a)
test_minus()