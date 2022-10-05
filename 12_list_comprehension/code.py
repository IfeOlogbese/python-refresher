numbers = [1,3,5]
doubled = [num * 2 for num in numbers]

print(doubled)

# With condition
friends = ['Rolf', 'Sam', 'Samantha', 'Jen', 'Saurah']
starts_s = [name for name in friends if name.startswith('S')]
print(starts_s)
print('friends', id(friends), 'starts_s', id(starts_s))