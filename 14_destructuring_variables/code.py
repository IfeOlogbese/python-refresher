x = (5, 11)
x = 5, 11
y, z = x
print('y', y, 'z', z)

student_attendance = {'Rolf': 96, "Adam": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    pass


person = ('Bob', 42, 'Mechanic')
name, _, profession = person

head, *tail = [1,2,3,4,5]
*head, tail = [1,2,3,4,5]
print(tail)
