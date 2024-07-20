items = [
    {"name": "Apple", "category": "Fruit"},
    {"name": "Banana", "category": "Fruit"},
    {"name": "Eggs", "category": "Protein"},
    {"name": "Milk", "category": "Protein"},
    {"name": "Donkey", "category": "Animal"},
    {"name": "Monkey", "category": "Animal"},
    {"name": "Bugatti", "category": "Car"},
    {"name": "Benz", "category": "Car"},
    {"name": "Chocolate", "category": "Dessert"},
    {"name": "Ice Cream", "category": "Dessert"},
    {"name": "Pizza", "category": "Grain"},
    {"name": "Pasta", "category": "Grain"},
    {"name": "Samsung", "category": "Phone"},
    {"name": "Coffee", "category": "Beverage"},
    {"name": "iPhone", "category": "Phone"},
]

categorized_items = {}

for item in items:
    category = item["category"]
    if category not in categorized_items:
        categorized_items[category] = []
    categorized_items[category].append(item["name"])

for category, items in categorized_items.items():
    print(f"{category}: {', '.join(items)}")
