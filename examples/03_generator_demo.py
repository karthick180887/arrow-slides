"""
Demo 3: Understanding Generators
A generator is a special iterator created with yield
Think of it as the KITCHEN preparing food ON-DEMAND (lazy evaluation)
"""

import sys
import time
from udupi_menu import ALL_ITEMS

print("=" * 70)
print("DEMO 3: GENERATORS - The Kitchen Preparing Food On-Demand")
print("=" * 70)

# Example 1: Basic Generator Function
print("\n🍳 Example 1: Basic Generator Function")
print("-" * 70)

def serve_menu():
    """Generator that yields menu items one by one"""
    print("  [Kitchen] Preparing first item...")
    yield "Masala Dosa"
    
    print("  [Kitchen] Preparing second item...")
    yield "Idli"
    
    print("  [Kitchen] Preparing third item...")
    yield "Filter Coffee"

print("Creating generator:")
kitchen = serve_menu()
print(f"Type: {type(kitchen)}")
print(f"Is it an iterator? {hasattr(kitchen, '__iter__') and hasattr(kitchen, '__next__')}")

print("\nRequesting items with next():")
print(f"Customer 1 gets: {next(kitchen)}")
print(f"Customer 2 gets: {next(kitchen)}")
print(f"Customer 3 gets: {next(kitchen)}")

# Example 2: Generator vs List - Memory Comparison
print("\n" + "=" * 70)
print("🍳 Example 2: Memory Efficiency - The Key Benefit!")
print("-" * 70)

# List approach (memory inefficient)
def make_all_dosas_list(count):
    """Make ALL dosas at once and store in list"""
    return [f"Dosa #{i}" for i in range(1, count + 1)]

# Generator approach (memory efficient)
def make_dosas_on_demand(count):
    """Make dosas one at a time on demand"""
    for i in range(1, count + 1):
        yield f"Dosa #{i}"

# Compare memory usage
items = 10000
dosa_list = make_all_dosas_list(items)
dosa_generator = make_dosas_on_demand(items)

list_size = sys.getsizeof(dosa_list)
gen_size = sys.getsizeof(dosa_generator)

print(f"Making {items:,} dosas:")
print(f"  List (all at once):     {list_size:,} bytes (~{list_size//1024} KB)")
print(f"  Generator (on-demand):  {gen_size} bytes")
print(f"\n  🎯 Generator uses {list_size // gen_size}x LESS memory!")
print(f"     That's why generators are MEMORY EFFICIENT!")

# Example 3: How yield works
print("\n" + "=" * 70)
print("🍳 Example 3: Understanding 'yield' Keyword")
print("-" * 70)

def kitchen_orders():
    """Demonstrate how yield pauses and resumes"""
    print("  👨‍🍳 Chef: Starting work...")
    
    print("  👨‍🍳 Chef: Making Dosa...")
    yield "Masala Dosa"
    print("  👨‍🍳 Chef: Dosa served, waiting for next order...")
    
    print("  👨‍🍳 Chef: Making Idli...")
    yield "Idli"
    print("  👨‍🍳 Chef: Idli served, waiting for next order...")
    
    print("  👨‍🍳 Chef: Making Coffee...")
    yield "Filter Coffee"
    print("  👨‍🍳 Chef: Coffee served, done for today!")

print("Taking orders:")
kitchen = kitchen_orders()
print("\n🔸 Customer 1 orders:")
item1 = next(kitchen)
print(f"   Received: {item1}\n")

print("🔸 Customer 2 orders:")
item2 = next(kitchen)
print(f"   Received: {item2}\n")

print("🔸 Customer 3 orders:")
item3 = next(kitchen)
print(f"   Received: {item3}\n")

print("💡 Notice: Function pauses at yield and resumes when next() is called!")

# Example 4: Generator Expression
print("\n" + "=" * 70)
print("🍳 Example 4: Generator Expression (Like List Comprehension)")
print("-" * 70)

menu = ["Masala Dosa", "Plain Dosa", "Idli", "Vada", "Pongal"]

# List comprehension (creates full list)
uppercase_list = [item.upper() for item in menu]
print(f"List comprehension: {uppercase_list}")
print(f"Type: {type(uppercase_list)}")
print(f"Memory: {sys.getsizeof(uppercase_list)} bytes")

# Generator expression (creates generator)
uppercase_gen = (item.upper() for item in menu)
print(f"\nGenerator expression: {uppercase_gen}")
print(f"Type: {type(uppercase_gen)}")
print(f"Memory: {sys.getsizeof(uppercase_gen)} bytes")

print("\nGetting items from generator:")
print(f"  First: {next(uppercase_gen)}")
print(f"  Second: {next(uppercase_gen)}")

# Example 5: Infinite Generator
print("\n" + "=" * 70)
print("🍳 Example 5: Infinite Generator (Continuous Orders)")
print("-" * 70)

def infinite_orders():
    """Generator that produces infinite stream of orders"""
    order_num = 1
    while True:
        yield f"Order #{order_num}: Masala Dosa"
        order_num += 1

print("Generating infinite orders:")
orders = infinite_orders()
for _ in range(5):
    print(f"  {next(orders)}")
print("  ... (can continue forever!)")

print("\n💡 Generators can represent infinite sequences!")
print("   Try this with a list and you'll run out of memory!")

# Example 6: Generator Pipeline
print("\n" + "=" * 70)
print("🍳 Example 6: Generator Pipeline (Chaining Generators)")
print("-" * 70)

def get_orders():
    """Step 1: Generate orders"""
    orders = ["Masala Dosa", "Plain Dosa", "Idli", "Vada"]
    for order in orders:
        yield order

def add_price(orders):
    """Step 2: Add prices to orders"""
    prices = {"Masala Dosa": 80, "Plain Dosa": 60, "Idli": 50, "Vada": 45}
    for order in orders:
        yield f"{order} - ₹{prices.get(order, 0)}"

def add_table_number(priced_orders, table):
    """Step 3: Add table number"""
    for order in priced_orders:
        yield f"Table {table}: {order}"

# Chain generators
print("Order processing pipeline:")
orders = get_orders()
priced = add_price(orders)
final = add_table_number(priced, 5)

for order in final:
    print(f"  ✓ {order}")

print("\n💡 Each generator processes one item at a time!")
print("   Memory efficient even with large data!")

# Example 7: Real-world use case - Daily Specials
print("\n" + "=" * 70)
print("🍳 Example 7: Real-World Use - Daily Specials Generator")
print("-" * 70)

def daily_specials():
    """Generate different specials for each day"""
    specials = {
        "Monday": "Masala Dosa + Coffee",
        "Tuesday": "Idli Vada Combo",
        "Wednesday": "Rava Dosa + Tea",
        "Thursday": "Pongal + Filter Coffee",
        "Friday": "Set Dosa + Badam Milk",
        "Saturday": "Uttapam + Tea",
        "Sunday": "Special Thali"
    }
    
    for day, special in specials.items():
        yield f"{day}: {special}"

print("This week's specials:")
for special in daily_specials():
    print(f"  🌟 {special}")

# Example 8: Generator vs List - Performance
print("\n" + "=" * 70)
print("🍳 Example 8: Performance Comparison")
print("-" * 70)

def list_approach(n):
    """Create list of n items"""
    return [f"Item {i}" for i in range(n)]

def generator_approach(n):
    """Generate n items"""
    for i in range(n):
        yield f"Item {i}"

n = 100000
print(f"Creating {n:,} menu items:\n")

# List approach
start = time.time()
items_list = list_approach(n)
first_item = items_list[0]
list_time = time.time() - start
list_mem = sys.getsizeof(items_list)

# Generator approach
start = time.time()
items_gen = generator_approach(n)
first_item = next(items_gen)
gen_time = time.time() - start
gen_mem = sys.getsizeof(items_gen)

print(f"List approach:")
print(f"  Time: {list_time:.4f} seconds")
print(f"  Memory: {list_mem:,} bytes\n")

print(f"Generator approach:")
print(f"  Time: {gen_time:.6f} seconds")
print(f"  Memory: {gen_mem} bytes\n")

print(f"🎯 Generator is {list_mem // gen_mem}x more memory efficient!")

# Example 9: Generator with state
print("\n" + "=" * 70)
print("🍳 Example 9: Generator Maintaining State")
print("-" * 70)

def order_tracker():
    """Track order numbers and maintain state"""
    order_count = 0
    total_sales = 0
    
    while True:
        order_count += 1
        item, price = yield f"Order #{order_count}"
        total_sales += price
        print(f"  💰 Total sales so far: ₹{total_sales}")

tracker = order_tracker()
next(tracker)  # Prime the generator

print("Processing orders:")
tracker.send(("Masala Dosa", 80))
tracker.send(("Idli", 50))
tracker.send(("Coffee", 30))

# Example 10: Common generator use cases
print("\n" + "=" * 70)
print("🍳 Example 10: Common Use Cases for Generators")
print("-" * 70)

# Reading large files
def read_large_menu(filename):
    """Read menu file line by line (memory efficient)"""
    # This is just a demo, not actually reading a file
    lines = [
        "Masala Dosa - ₹80",
        "Plain Dosa - ₹60",
        "Idli - ₹50"
    ]
    for line in lines:
        yield line.strip()

print("Reading large menu file:")
for line in read_large_menu("menu.txt"):
    print(f"  {line}")

# Filtering data
def expensive_items(menu, min_price):
    """Filter items above minimum price"""
    prices = {"Masala Dosa": 80, "Plain Dosa": 60, "Idli": 50, "Vada": 45}
    for item in menu:
        if prices.get(item, 0) >= min_price:
            yield item

print(f"\nItems ≥ ₹60:")
menu_items = ["Masala Dosa", "Plain Dosa", "Idli", "Vada"]
for item in expensive_items(menu_items, 60):
    print(f"  • {item}")

print("\n" + "=" * 70)
print("✅ SUMMARY: Generators")
print("=" * 70)
print("""
1. Generators use 'yield' keyword instead of 'return'
2. Created with generator functions or expressions
3. Extremely memory efficient (lazy evaluation)
4. Items created on-demand, not all at once
5. Can represent infinite sequences
6. Perfect for large datasets or streams
7. Can be chained in pipelines
8. Think: Kitchen making food only when ordered

KEY DIFFERENCE from Lists:
- List: Make ALL 10,000 dosas NOW (uses lots of memory)
- Generator: Make dosa ONLY when customer asks (minimal memory)
""")
