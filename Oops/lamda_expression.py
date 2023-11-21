from functools import reduce
def func1(x): return x * 2  # same as ->  func2 = lambda x: x * 2


print(func1(5))
# print(func2(5))


lst = [2, 3, 4, 5]
lst = list(filter(lambda x: (x % 2 == 0), lst))
print(lst)

lst = [0, 2, 3, 4, 5]
lst = list(filter(lambda x: x / 3, lst))
print(lst)

lst = [0, 2, 3, 4, 5]
lst = list(map(lambda x: x / 3, lst))
print(lst)


lst = [1, 2, 3, 4, 5]
lst = reduce(lambda x, y: x * y, lst)
print(lst)
