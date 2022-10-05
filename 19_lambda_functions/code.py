def add(x, y): return x + y


print(add(2, 2))

# use as one word
print((lambda x, y: x + y)(3, 2))


def double(x):
    return x * 2


sequence = [1, 2, 3, 4, 5]
doubled = [double(x) for x in sequence]
doubled = map(double, sequence)
print(list(doubled))
print(sum(map(lambda x: x * 2, sequence)))
