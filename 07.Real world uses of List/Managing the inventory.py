# Inventory Management using List

# Inventory format: [id, name, quantity, price]
inventory = []

# Function to add item
def add_item(item_id, name, quantity, price):
    inventory.append([item_id, name, quantity, price])
    print(f"✅ {name} added to inventory.")

# Function to update quantity
def update_quantity(item_id, new_quantity):
    for item in inventory:
        if item[0] == item_id:
            item[2] = new_quantity
            print(f"🔄 Quantity updated for {item[1]}.")
            return
    print("❌ Item not found.")

# Function to remove item
def remove_item(item_id):
    for item in inventory:
        if item[0] == item_id:
            inventory.remove(item)
            print(f"🗑️ {item[1]} removed from inventory.")
            return
    print("❌ Item not found.")

# Function to display all items
def display_inventory():
    if not inventory:
        print("📦 Inventory is empty.")
        return
    print("\n------ Inventory ------")
    print("ID | Name       | Quantity | Price")
    print("-------------------------------")
    for item in inventory:
        print(f"{item[0]}  | {item[1]:10} | {item[2]:8} | {item[3]}")
    print("-------------------------------\n")

# ---- Example Usage ----
add_item(1, "Laptop", 10, 50000)
add_item(2, "Mouse", 50, 500)
add_item(3, "Keyboard", 30, 1500)

display_inventory()

update_quantity(2, 60)   # Update Mouse quantity
remove_item(3)           # Remove Keyboard

display_inventory()
