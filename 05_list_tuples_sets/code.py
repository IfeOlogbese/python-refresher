l = ['Bob', 'Rolf', 'Anne']
t = ('Bob', 'Rolf', 'Anne')
s = {'Bob', 'Rolf', 'Anne'}

print(l[0])
print(t[0])

# You can edit a list by their index, can't modify tuples or set
l[0] = 'Ife'

# Add to list using append, can't append tuple
l.append('Ologbese')


# Removing from a list
l.remove('Ologbese')

# Add to set
s.add('Ologbese')

print(l)
print(f'Set {s}')