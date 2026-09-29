students = {
    "Ana": 85,
    "Ben": 90,
    "Carlo": 78,
    "Diana": 95
}
print("STUDENT GRADES")
print("----------------")
print("Ana:", students["Ana"])
print("Ben:", students["Ben"])

# Add a new student
students["Ella"] = 88

# Update a student's grade
students["Carlo"] = 82
students["Diana"] = 91

name1 = input("\nEnter your name: ")
grade1 = int(input("Enter grade: "))
students[name1] = grade1

print(students)
print("\nUpdated Student Grades")
print("---------------------------")

for name, grade in students.items():
    print(name, ":", grade)
