import json

INVENTORY_FILE = "inventory.json"

def load_inventory():
    with open(INVENTORY_FILE, "r") as file:
        return json.load(file)

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)

def add_item(inventory):
    item_id = input("Enter item ID: ")
    if item_id in inventory:
        print("Item ID already exists!")
        return
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    inventory[item_id] = {"name": name, "quantity": quantity, "price": price}
    save_inventory(inventory)
    print("Item added successfully!")

def update_item(inventory):
    item_id = input("Enter item ID to update: ")
    if item_id not in inventory:
        print("Item not found!")
        return
    name = input("Enter new name (leave blank to keep existing): ") or inventory[item_id]["name"]
    quantity = input("Enter new quantity (leave blank to keep existing): ")
    price = input("Enter new price (leave blank to keep existing): ")
    inventory[item_id]["name"] = name
    inventory[item_id]["quantity"] = int(quantity) if quantity else inventory[item_id]["quantity"]
    inventory[item_id]["price"] = float(price) if price else inventory[item_id]["price"]
    save_inventory(inventory)
    print("Item updated successfully!")

def view_inventory(inventory):
    if not inventory:
        print("No items in inventory.")
        return
    for item_id, details in inventory.items():
        print(f"ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}, Price: {details['price']}")

def search_item(inventory):
    name = input("Enter item name to search: ").lower()
    found = False
    for item_id, details in inventory.items():
        if name in details["name"].lower():
            print(f"ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}, Price: {details['price']}")
            found = True
    if not found:
        print("Item not found.")

def main():
    inventory = load_inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Search Item")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            update_item(inventory)
        elif choice == "3":
            view_inventory(inventory)
        elif choice == "4":
            search_item(inventory)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
