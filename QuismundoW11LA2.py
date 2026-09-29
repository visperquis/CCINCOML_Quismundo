pizza_flavors = (("Pizzette", 1000),("Pizza Margherita", 1200),("Pizza Alla Diavola", 1300),("Pizza Parmigiano", 1550))

pizza_sizes = (("Small", 0),("Medium", 200),("Large", 400))

orders = []
while True:

    print("===== PIZZA MENU =====")
    print("\nPizza Flavors:")
    print("1. Pizzette - ₱1000")
    print("2. Pizza Margherita - ₱1200")
    print("3. Pizza Alla Diavola - ₱1300")
    print("4. Pizza Parmigiano - ₱1550")

    flavor_choice = input("\nChoose your pizza flavor (1-4): ")

    match flavor_choice:
        case "1":
            flavor = pizza_flavors[0]
        case "2":
            flavor = pizza_flavors[1]
        case "3":
            flavor = pizza_flavors[2]
        case "4":
            flavor = pizza_flavors[3]
        case _:
            print("Invalid choice!")
            continue

    print("\nPizza Sizes:")
    print("1. Small - No additional charge")
    print("2. Medium - +200")
    print("3. Large - +400")

    size_choice = input("Choose your pizza size (1-3): ")

    match size_choice:
        case "1":
            size = pizza_sizes[0]
        case "2":
            size = pizza_sizes[1]
        case "3":
            size = pizza_sizes[2]
        case _:
            print("Invalid choice!")
            continue

    quantity = int(input("Enter quantity: "))

    price = flavor[1] + size[1]
    total = price * quantity
    orders.append((flavor[0], size[0], quantity, total))

    print("\nPizza added to your order!")

    again = input("Do you want to order another pizza? (Yes/No): ").title()

    if again != "Yes":
        break

print("\nORDER SUMMARY")
grand_total = 0

for order in orders:
    flavor = order[0]
    size = order[1]
    quantity = order[2]
    total = order[3]

    print("\nPizza:", flavor)
    print("Size:", size)
    print("Quantity:", quantity)
    print("Total: ", total)
print("Thank you for ordering!")

