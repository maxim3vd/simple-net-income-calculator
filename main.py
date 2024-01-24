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
