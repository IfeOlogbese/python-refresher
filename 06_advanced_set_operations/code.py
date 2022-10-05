from threading import local


friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}
local = {'Rolf'}

# difference between sets
local_friends = friends.difference(abroad)
print(local_friends)

# unite two sets
friends = local.union(abroad)

# intersection

both = friends.intersection(abroad)
print(both)
