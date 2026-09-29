for i in range(10):
    print(i)

i = 10
while i >= 1:
    print(i)
    i -= 1

word = "HALIZA"
for character in word:
    print(character)

while True:
    name = input("Enter your name: ")
    print("Hello,", name)

    again = input("Do you want to enter again? (Y/N): ")

    if again.upper() != "Y":
        print("Program Ended.")
        break
total=100
i=1
while(i<=50):
    total=total+i
    i=i+1
    print("The sum is:",total)
