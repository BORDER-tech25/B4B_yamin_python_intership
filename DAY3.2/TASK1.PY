def marks_summary(marks):
    lowest = min(marks)
    highest = max(marks)
    average = sum(marks) / len(marks)
    return (lowest, highest, average)

student_marks = [78, 92, 65, 88, 74]

low, high, avg = marks_summary(student_marks)

print("Lowest:", low)
print("Highest:", high)
print("Average:", avg)