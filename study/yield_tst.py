


def fun():
    print(11)
    yield 1
    print(22)
    yield 2
    print(33)
    yield 3

f1 = fun()


a = next(f1)
print('a = next(f1) -> a = ',a)

a = next(f1)
print('a = next(f1) -> a = ',a)

a = next(f1)
print('a = next(f1) -> a = ',a)

a = next(f1)
print('a = next(f1) -> a = ',a)
