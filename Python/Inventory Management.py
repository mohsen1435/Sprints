
inv = []

sold_items = []

def add():
    name = input("Enter item name: ").upper()
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    inv.append({"n": name, "p": price, "q": quantity})
    print("Item added successfully.")
    print("Current Inventory")
    print(inv)

def update():
    while True:
        print("1. Add New Items")
        print("2. Add Sold Items")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item_name = input("Enter the name of the item to update stock: ").upper()
            for item in inv:
                if item["n"] == item_name:
                    new_quantity = int(input("Enter the new quantity: "))
                    item["q"] = new_quantity
                    print("Stock updated successfully.")
                    return
            else:
                new_quantity = int(input("Enter the quantity of the new item: "))
                inv.append({"n": item_name, "q": new_quantity})
                print("New item added successfully.")
                return
        elif choice == "2":
            item_name = input("Enter the name of the item sold: ").upper()
            for item in inv:
                if item["n"] == item_name:
                    sold_quantity = int(input("Enter the quantity sold: "))
                    if sold_quantity <= item["q"]:
                        item["q"] -= sold_quantity
                        sold_items.append({"n": item_name, "q": sold_quantity})
                        print("Stock updated successfully.")
                        return
                    else:
                        print("Error: Sold quantity exceeds available quantity.")
                        return
            else:
                print("Item not found in inventory.")
                return
        else:
            print("Invalid choice. Please choose again.")


def sales():
    print("Sales Report:")
    total_revenue = 0
    for item in sold_items:
        for product in inv:
            if product["n"] == item["n"]:
                revenue = product["p"] * item["q"]
                total_revenue += revenue
                print(f"Item: {product['n']}, Quantity Sold: {item['q']}, Revenue: ${revenue}")
    print(f"Total Revenue: ${total_revenue}")


def popular():
    s_items = sorted(sold_items, key=lambda x: x["q"], reverse=True)
    print("Top Three Most Popular Items:")
    for item in s_items[:3]:
        print(f"Item: {item['n']}, Quantity Sold: {item['q']}")  

while True:
    print("1. Add New Item")
    print("2. Update Stock")
    print("3. Generate Sales Report")
    print("4. Popular Items")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
         add()
    elif choice == "2":
        update()
    elif choice == "3":
        sales()
    elif choice == "4":
        popular()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please choose again.")
