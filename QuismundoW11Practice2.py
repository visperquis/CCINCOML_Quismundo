# Dictionary and List
students = {"Ana": [90, 85, 82],
            "Kirk": [72, 73, 78]
            }
for name, grade in students.items():
    print(name, *grade)

# Dictionary and Tuple
students = {
    "Ana": (90, 85, 82),
    "Kirk": (72, 73, 78)
}

for name, grade in students.items():
    print(name, *grade)