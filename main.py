# Dictionary mapping item names to their respective prices and quantities
items = {
    "Bubblegum": {"price": 2, "quantity": 101},
    "Toffee": {"price": 0.2, "quantity": 590},
    "Ice cream": {"price": 5, "quantity": 450},
    "Milk chocolate": {"price": 4, "quantity": 420},
    "Doughnut": {"price": 2.5, "quantity": 430},
    "Pancake": {"price": 3.2, "quantity": 25}
}

# Display the header "Earned amount:"
print("Earned amount:")

# Calculate and display the earned amount for each item
for item, data in items.items():
    print(f"{item}: ${round(data['price'] * data['quantity'])}")

# Calculate and display the total income
total_income = sum(item["price"] * item["quantity"] for item in items.values())
print("\nIncome:", f"${int(total_income) if total_income.is_integer() else total_income}")

# Ask users for staff expenses
staff_expenses = float(input("Staff expenses: "))

# Ask users for other expenses
other_expenses = float(input("Other expenses: "))
