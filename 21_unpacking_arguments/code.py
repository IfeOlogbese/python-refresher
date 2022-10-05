# pack arguments into a single param
def multiply(*args):
    print(args)


multiply(1, 3, 5)


# destructure arguments


def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))

nums = {'x': 2, 'y': 5}
print(add(**nums))


# args and named operator
def apply(*args, operator):
    pass


print(apply(1, 2, 4, 5, operator='*'))
