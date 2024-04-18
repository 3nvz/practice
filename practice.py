
grades = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

student = grades.get("Malika")
gradesAdded, averageGrade = 0, 0

for grade in student:
    gradesAdded += grade

averageGrade = gradesAdded/len(student)

print("{:.2f}".format(averageGrade))
