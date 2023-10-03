#Program that manages shoe stock in a warehouse

#Import
from tabulate import tabulate

#========The beginning of the class==========

#Shoe class
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        pass
        return self.cost

    def get_quantity(self):
        pass
        return self.quantity

    def __str__(self):
        pass
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

#=============Shoe list===========

shoe_list = []

#==========Functions outside the class==============

#Function that reads the shoes data from the inventory txt file
def read_shoes_data():
    pass
    try:
        with open("inventory.txt", "r") as file:
            #Skipping the first line
            next(file) 
            #Starting from line 2
            for line_number, line in enumerate(file, start=2): 
                line = line.strip()
                data = line.split(",")
                if len(data) != 5:
                    print(f"Error: Incorrect data format in line {line_number}. Skipping.")
                    continue
                
                country, code, product, cost, quantity = data
                cost = float(cost)
                quantity = int(quantity)
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error: File 'inventory.txt' not found.")

#Function that allows the users to capture new shoes which will be added to the inventory file
def capture_shoes():
    pass
    print("Enter shoe details:")
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = int(input("Cost: "))
    quantity = int(input("Quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("\nShoe data captured successfully.")

    try:
        with open("inventory.txt", "a") as file:
            file.write(f"\n{country},{code},{product},{cost},{quantity}\n")
    except IOError:
        print("Error: Unable to write to the file 'inventory.txt'.")

#Function that allows users to view all the shoes that is in the inventory file
def view_all():
    pass
    if len(shoe_list) == 0:
        print("No shoes data available.")
        return

    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    shoe_data = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_list]
    print("\nShoe Inventory\n")
    print(tabulate(shoe_data, headers=headers, tablefmt="grid"))

#Function that allows users to restock current low-stock items in the inventory file
def re_stock():
    if len(shoe_list) == 0:
        print("No shoes data available.")
        return

    min_quantity_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"Shoe to re-stock: {min_quantity_shoe}")
    choice = input("Do you want to add this quantity? (yes/no): ").lower()

    if choice == "yes":
        new_quantity = int(input("Enter the new quantity: "))
        min_quantity_shoe.quantity += new_quantity
        print("\nShoe quantity updated successfully.")

        # Update the inventory.txt file with the new quantity
        try:
            with open("inventory.txt", "r") as file:
                lines = file.readlines()

            with open("inventory.txt", "w") as file:
                # Write the header line back
                file.write(lines[0]) 
                for line in lines[1:]:
                    country, code, product, cost, quantity = line.strip().split(",")
                    if code == min_quantity_shoe.code:
                        quantity = min_quantity_shoe.quantity
                    file.write(f"{country},{code},{product},{cost},{quantity}\n")
        except IOError:
            print("Error: Unable to write to the file 'inventory.txt'.")
    else:
        print("Shoe quantity not updated.")

#Function that searches for a specific shoe by code
def search_shoe():
    pass
    if len(shoe_list) == 0:
        print("No shoes data available.")
        return

    code = input("Enter the code of the shoe to search: ")
    found_shoe = None

    for shoe in shoe_list:
        if shoe.code == code:
            found_shoe = shoe
            break

    if found_shoe:
        print("\nFound Shoe:\n", found_shoe)
    else:
        print("Shoe with the given code not found.")

#Function that shoes total value of each shoe item by stock amount and price
def value_per_item():
    pass
    if len(shoe_list) == 0:
        print("No shoes data available.")
        return

    print("\nValue per Item\n")
    headers = ["Product", "Value"]
    value_data = [[shoe.product, shoe.cost * shoe.quantity] for shoe in shoe_list]
    print(tabulate(value_data, headers=headers, tablefmt="grid"))

#Function that allows users to see what shoe has the highest quantity stock
def highest_qty():
    pass
    if len(shoe_list) == 0:
        print("No shoes data available.")
        return

    max_quantity_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"\nHighest Quantity Shoe: \n{max_quantity_shoe}")

#==========Main Menu=============
def display_menu():
    print("\n====== Main Menu ======")
    print("1. Read Shoes Data")
    print("2. Capture Shoes")
    print("3. View All Shoes")
    print("4. Re-stock Shoes")
    print("5. Search for a Shoe")
    print("6. Calculate Value per Item")
    print("7. Show Shoe with Highest Quantity")
    print("8. Exit")
    print("========================")

#Function that displays the menu and lets the user input which action to take
def main():

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-8).")

#Calling the main function
main()