friends = ['Rolf', 'Bob', 'Jen']
print('Jen' in friends)

movies_watched = {'The Matrix', 'Green Book', 'Her'}
user_movie = input('Enter something you watched recently: ')

if user_movie in movies_watched:
    print(f'I have watched {user_movie} too!')
else:
    print('I haven\'t watched that yet')
