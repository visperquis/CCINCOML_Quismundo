Quismundo_classrecord = {
    "Blossom": {
        "studID": "5001",
        "Grade": [90, 85, 86, 82, 83, 90, 92]
    },
    "Buttercup": {
        "studID": "5002",
        "Grade": [72, 75, 60, 80, 84, 75, 85]
    },
    "Bubbles": {
        "studID": "5003",
        "Grade": [89, 78, 90, 78, 86, 59, 91]
    }
}

Quismundo_search = input("Enter student name to search: ")

if Quismundo_search in Quismundo_classrecord:
    student = Quismundo_classrecord[Quismundo_search]
    Quismundo_grades = student["Grade"]

    Quismundo_average = sum(Quismundo_grades) / len(Quismundo_grades)

    print("\nStudent found!")
    print("Student:", Quismundo_search)
    print("Student ID:", student["studID"])
    print("Grades:", Quismundo_grades)
    print("Average:", round(Quismundo_average, 3))

    if any(grade < 60 for grade in Quismundo_grades):
        print("Candidate for intervention")
    else:
        print("No grade below 60")

    print("Highest Grade:", max(Quismundo_grades))
    print("Lowest Grade:", min(Quismundo_grades))

else:
    print("\nStudent not found.")









