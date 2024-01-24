# Dictionary mapping item names to their respective prices
items = {
    "Bubblegum": {"price": 2},
    "Toffee": {"price": 0.2},
    "Ice cream": {"price": 5},
    "Milk chocolate": {"price": 4},
    "Doughnut": {"price": 2.5},
    "Pancake": {"price": 3.2}
}

# Display the header "Prices:"
print("Prices:")

# Display the list of items and prices
for item, data in items.items():
    print(f"{item}: ${data['price']}")
