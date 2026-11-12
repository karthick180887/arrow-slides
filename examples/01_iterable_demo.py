"""
Demo 1: Understanding Iterables
An iterable is any Python object that can return an iterator
Think of it as the MENU CARD at Udupi Garden - you can look through all items
"""

import sys
from udupi_menu import UDUPI_MENU, ALL_ITEMS, POPULAR_ITEMS

print("=" * 70)
print("DEMO 1: ITERABLES - The Udupi Garden Menu Card")
print("=" * 70)

# Example 1: Lists are iterables
print("\n📋 Example 1: The Menu Card (List)")
print("-" * 70)
menu_items = ["Masala Dosa", "Plain Dosa", "Idli", "Vada", "Pongal"]
print(f"Menu items: {menu_items}")
print(f"Type: {type(menu_items)}")
print(f"Is iterable? {hasattr(menu_items, '__iter__')}")

# You can iterate over it multiple times
print("\n🔄 We can look at the menu multiple times:")
for i in range(2):
    print(f"\nPass {i+1}:")
    for item in menu_items:
        print(f"  - {item}")

# Example 2: Tuples are iterables
print("\n" + "=" * 70)
print("📋 Example 2: Popular Combo (Tuple)")
print("-" * 70)
combo = ("Idli", "Vada", "Filter Coffee")
print(f"Combo items: {combo}")
print(f"Type: {type(combo)}")
print(f"Is iterable? {hasattr(combo, '__iter__')}")

# Example 3: Strings are iterables
print("\n" + "=" * 70)
print("📋 Example 3: Restaurant Name (String)")
print("-" * 70)
restaurant = "UDUPI"
print(f"Restaurant: {restaurant}")
print(f"Is iterable? {hasattr(restaurant, '__iter__')}")
print("Letters:", end=" ")
for letter in restaurant:
    print(letter, end=" ")
print()

# Example 4: Dictionaries are iterables
print("\n" + "=" * 70)
print("📋 Example 4: Menu Categories (Dictionary)")
print("-" * 70)
categories = {
    "Breakfast": "Idli, Dosa, Pongal",
    "Snacks": "Vada, Samosa",
    "Beverages": "Coffee, Tea"
}
print(f"Is dictionary iterable? {hasattr(categories, '__iter__')}")
print("\nIterating over keys:")
for category in categories:
    print(f"  - {category}: {categories[category]}")

# Example 5: Checking if something is iterable
print("\n" + "=" * 70)
print("📋 Example 5: How to Check if Something is Iterable")
print("-" * 70)

def is_iterable(obj):
    """Check if object is iterable"""
    return hasattr(obj, '__iter__')

test_objects = [
    ("List", ["Dosa", "Idli"]),
    ("String", "Udupi"),
    ("Number", 42),
    ("Dictionary", {"item": "Dosa"}),
]

for name, obj in test_objects:
    print(f"{name:15} -> Iterable: {is_iterable(obj)}")

# Example 6: Getting an iterator from an iterable
print("\n" + "=" * 70)
print("📋 Example 6: Converting Iterable to Iterator")
print("-" * 70)
menu = ["Masala Dosa", "Idli", "Vada"]
print(f"Original menu (iterable): {menu}")

# Get iterator using iter()
menu_iterator = iter(menu)
print(f"Iterator object: {menu_iterator}")
print(f"Type: {type(menu_iterator)}")

# Key point: Every iterable can give you an iterator
print("\n💡 KEY POINT:")
print("   An ITERABLE is like a MENU CARD")
print("   - You can look at it multiple times")
print("   - All items are visible")
print("   - It has __iter__() method that returns an iterator")

# Example 7: Memory comparison
print("\n" + "=" * 70)
print("📋 Example 7: Memory Usage of Iterables")
print("-" * 70)

small_menu = ["Dosa", "Idli", "Vada"]
large_menu = ALL_ITEMS  # All 52 items from udupi_menu

print(f"Small menu (3 items): {sys.getsizeof(small_menu)} bytes")
print(f"Large menu ({len(large_menu)} items): {sys.getsizeof(large_menu)} bytes")
print(f"\n⚠️  Notice: Lists store ALL items in memory at once!")

# Example 8: Real-world use case
print("\n" + "=" * 70)
print("📋 Example 8: Real-World Use - Menu Display")
print("-" * 70)

def display_category_menu(category_name):
    """Display all items in a category"""
    items = UDUPI_MENU.get(category_name, [])
    print(f"\n{category_name} Menu:")
    print("-" * 40)
    for idx, item in enumerate(items, 1):
        print(f"{idx:2}. {item}")

display_category_menu("Dosas")

print("\n" + "=" * 70)
print("✅ SUMMARY: Iterables")
print("=" * 70)
print("""
1. An iterable is any object that can return an iterator
2. Common iterables: list, tuple, string, dict, set
3. Check with: hasattr(obj, '__iter__')
4. Can be iterated multiple times
5. All items stored in memory
6. Think: Menu card you can read again and again
""")
