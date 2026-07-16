students = [
    ("Riya", 88),
    ("Aman", 95),
    ("Sara", 72),
    ("Karan", 91)
]

sorted_students = sorted(students, key=lambda student: student[1], reverse=True)

print("Sorted Students:", sorted_students)
