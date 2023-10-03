class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.product} ({self.code}) from {self.country}, Cost: {self.cost}, Quantity: {self.quantity}"

shoes_list = []

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # skip the first line
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                cost = float(cost)
                quantity = int(quantity)
                shoe = Shoe(country, code, product, cost, quantity)
                shoes_list.append(shoe)
    except FileNotFoundError:
        print("Error: File 'inventory.txt' not found.")

def capture_shoes():
    print("Enter shoe details:")
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = float(input("Cost: "))
    quantity = int(input("Quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)

def view_all():
    for shoe in shoes_list:
        print(shoe)

def view_highest_quantity():
    highest_quantity_shoe = max(shoes_list, key=lambda x: x.quantity)
    print("Shoe with highest quantity:")
    print(highest_quantity_shoe)

def restock_shoes():
    code = input("Enter the code of the shoe to restock: ")
    for shoe in shoes_list:
        if shoe.code == code:
            quantity_to_add = int(input("Enter the quantity to add: "))
            shoe.quantity += quantity_to_add
            print(f"{quantity_to_add} units of {shoe.product} added to the inventory.")
            break
    else:
        print("Shoe not found.")

def value_per_item():
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"Value of {shoe.product}: {value}")

# Main program
read_shoes_data()

while True:
    print("\n======== Shoe Inventory Management Menu =======")
    print("1. Capture Shoe")
    print("2. View All Shoes")
    print("3. View Shoe with Highest Quantity")
    print("4. Restock Shoes")
    print("5. Calculate Value per Item")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        capture_shoes()
    elif choice == '2':
        view_all()
    elif choice == '3':
        view_highest_quantity()
    elif choice == '4':
        restock_shoes()
    elif choice == '5':
        value_per_item()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
