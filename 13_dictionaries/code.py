friend_ages = {'Rolf': 24, "Adam": 30, "Anne": 27}
friend_ages["Bob"] = 20

print(friend_ages)

friends = [
    {'name': 'Rolf', 'age': 20},
    {'name': 'Kevin', 'age': 23},
    {'name': 'Poke', 'age': 26},
]

student_attendance = {'Rolf': 96, "Adam": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(student)


# Check membership
if 'Bob' in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print('Bob is not a student in this class.')

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))
