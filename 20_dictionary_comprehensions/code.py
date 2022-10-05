users = [
    (0, 'Bob', 'password'),
    (1, 'Rolf', 'password'),
    (2, 'Jose', 'yret'),
    (3, 'username', '234'),
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)