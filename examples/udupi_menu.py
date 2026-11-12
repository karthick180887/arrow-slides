"""
Udupi Garden Restaurant Menu Data
Complete menu with authentic South Indian food items
"""

# Complete Udupi Garden Menu organized by categories
UDUPI_MENU = {
    "Dosas": [
        "Plain Dosa",
        "Masala Dosa",
        "Butter Dosa",
        "Butter Masala Dosa",
        "Ghee Dosa",
        "Ghee Masala Dosa",
        "Rava Dosa",
        "Rava Masala Dosa",
        "Rava Onion Dosa",
        "Rava Onion Masala Dosa",
        "Onion Dosa",
        "Mysore Masala Dosa",
        "Paneer Dosa",
        "Paneer Masala Dosa",
        "Set Dosa",
        "Paper Plain Dosa",
        "Paper Masala Dosa",
        "Cheese Dosa",
        "Cheese Masala Dosa",
    ],
    "Idlis": [
        "Idli (2 pieces)",
        "Idli (3 pieces)",
        "Idli (4 pieces)",
        "Set Idli",
        "Ghee Idli",
    ],
    "Vadas": [
        "Medu Vada (2 pieces)",
        "Masala Vada",
        "Sambar Vada",
        "Dahi Vada",
    ],
    "Uttapams": [
        "Plain Uttapam",
        "Onion Uttapam",
        "Tomato Onion Uttapam",
        "Vegetable Uttapam",
        "Cheese Uttapam",
    ],
    "Rice Items": [
        "Sambhar Rice",
        "Curd Rice",
        "Pongal",
        "Rava Pongal",
        "Lemon Rice",
        "Tamarind Rice",
    ],
    "Bread Items": [
        "Puri (2 pieces)",
        "Puri (3 pieces)",
        "Chapati (2 pieces)",
        "Paratha",
    ],
    "Beverages": [
        "Filter Coffee",
        "Tea",
        "Badam Milk",
        "Horlicks",
        "Bournvita",
    ],
    "Combo Meals": [
        "Idli Vada Combo",
        "Dosa Coffee Combo",
        "Pongal Coffee Combo",
        "South Indian Thali",
    ]
}

# Flat list of all menu items (for iteration examples)
ALL_ITEMS = []
for category, items in UDUPI_MENU.items():
    ALL_ITEMS.extend(items)

# Popular items (mentioned in the video)
POPULAR_ITEMS = ["Idli (2 pieces)", "Masala Dosa", "Pongal", "Puri (2 pieces)"]

# Menu with prices (for realistic examples)
MENU_WITH_PRICES = {
    "Masala Dosa": 80,
    "Plain Dosa": 60,
    "Rava Dosa": 90,
    "Set Idli": 50,
    "Medu Vada (2 pieces)": 45,
    "Pongal": 70,
    "Puri (2 pieces)": 55,
    "Filter Coffee": 30,
    "Sambhar Rice": 85,
    "Curd Rice": 70,
}

def get_category_items(category):
    """Get all items in a specific category"""
    return UDUPI_MENU.get(category, [])

def get_all_dosas():
    """Get all dosa varieties"""
    return UDUPI_MENU["Dosas"]

def get_item_price(item):
    """Get price of an item"""
    return MENU_WITH_PRICES.get(item, 0)

def display_menu():
    """Display the complete menu"""
    print("=" * 50)
    print("UDUPI GARDEN RESTAURANT MENU")
    print("=" * 50)
    for category, items in UDUPI_MENU.items():
        print(f"\n{category}:")
        print("-" * 50)
        for item in items:
            price = MENU_WITH_PRICES.get(item, "Price on request")
            print(f"  • {item:30} {price if isinstance(price, str) else f'₹{price}'}")
    print("=" * 50)

if __name__ == "__main__":
    display_menu()
    print(f"\nTotal items on menu: {len(ALL_ITEMS)}")
