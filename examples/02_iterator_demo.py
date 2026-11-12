"""
Demo 2: Understanding Iterators
An iterator is an object that remembers its position during iteration
Think of it as the WAITER taking orders one by one from the menu
"""

import sys
from udupi_menu import ALL_ITEMS

print("=" * 70)
print("DEMO 2: ITERATORS - The Waiter Taking Orders")
print("=" * 70)

# Example 1: Creating an iterator from an iterable
print("\n🙋 Example 1: Creating an Iterator")
print("-" * 70)
menu = ["Masala Dosa", "Idli", "Vada", "Pongal"]
print(f"Menu (iterable): {menu}")

# Convert to iterator
menu_iter = iter(menu)
print(f"Iterator: {menu_iter}")
print(f"Type: {type(menu_iter)}")

# Example 2: Using next() to get items one by one
print("\n" + "=" * 70)
print("🙋 Example 2: Getting Items with next()")
print("-" * 70)

menu = ["Masala Dosa", "Idli", "Vada"]
orders = iter(menu)

print("Customer 1 orders:", next(orders))
print("Customer 2 orders:", next(orders))
print("Customer 3 orders:", next(orders))

# What happens when we run out of items?
print("\n⚠️  What happens when no more items?")
try:
    print("Customer 4 orders:", next(orders))
except StopIteration:
    print("❌ StopIteration exception raised - No more items!")

# Example 3: Iterator vs Iterable - Can you iterate twice?
print("\n" + "=" * 70)
print("🙋 Example 3: Iterator vs Iterable - Multiple Passes")
print("-" * 70)

menu = ["Dosa", "Idli", "Vada"]

print("✅ ITERABLE (List) - Multiple passes possible:")
for i in range(2):
    print(f"  Pass {i+1}:", end=" ")
    for item in menu:
        print(item, end=" ")
    print()

print("\n❌ ITERATOR - Only one pass possible:")
menu_iter = iter(menu)
print("  Pass 1:", end=" ")
for item in menu_iter:
    print(item, end=" ")
print("\n  Pass 2:", end=" ")
for item in menu_iter:
    print(item, end=" ")
print("(Nothing! Iterator is exhausted)")

# Example 4: How for loop uses iterators internally
print("\n" + "=" * 70)
print("🙋 Example 4: How 'for' Loop Works (Behind the Scenes)")
print("-" * 70)

menu = ["Dosa", "Idli"]

print("What Python does when you write 'for item in menu':")
print("\n1. Calls iter(menu) to get an iterator")
menu_iter = iter(menu)
print(f"   Iterator: {menu_iter}")

print("\n2. Calls next() repeatedly until StopIteration")
try:
    while True:
        item = next(menu_iter)
        print(f"   Got: {item}")
except StopIteration:
    print("   StopIteration - loop ends")

# Example 5: Custom Iterator Class
print("\n" + "=" * 70)
print("🙋 Example 5: Creating a Custom Iterator Class")
print("-" * 70)

class UdupiMenuIterator:
    """Custom iterator for Udupi Garden menu items"""
    
    def __init__(self, items):
        self.items = items
        self.index = 0
    
    def __iter__(self):
        """Return the iterator object itself"""
        return self
    
    def __next__(self):
        """Return the next item or raise StopIteration"""
        if self.index >= len(self.items):
            raise StopIteration
        
        item = self.items[self.index]
        self.index += 1
        return item

menu_items = ["Masala Dosa", "Idli", "Filter Coffee"]
print(f"Menu: {menu_items}")

menu_iterator = UdupiMenuIterator(menu_items)
print("\nServing orders:")
print(f"Order 1: {next(menu_iterator)}")
print(f"Order 2: {next(menu_iterator)}")
print(f"Order 3: {next(menu_iterator)}")

try:
    print(f"Order 4: {next(menu_iterator)}")
except StopIteration:
    print("Order 4: ❌ No more items!")

# Example 6: Iterator Protocol
print("\n" + "=" * 70)
print("🙋 Example 6: The Iterator Protocol")
print("-" * 70)

print("An object is an iterator if it has:")
print("  1. __iter__() method - returns self")
print("  2. __next__() method - returns next item or raises StopIteration")

menu = ["Dosa", "Idli"]
menu_iter = iter(menu)

print(f"\nHas __iter__? {hasattr(menu_iter, '__iter__')}")
print(f"Has __next__? {hasattr(menu_iter, '__next__')}")
print(f"Is iterator? {hasattr(menu_iter, '__iter__') and hasattr(menu_iter, '__next__')}")

# Example 7: Memory efficiency
print("\n" + "=" * 70)
print("🙋 Example 7: Memory Efficiency")
print("-" * 70)

# Create large menu
large_menu = ALL_ITEMS * 200  # 52 * 200 = 10,400 items
large_iterator = iter(large_menu)

print(f"Large menu list: {sys.getsizeof(large_menu):,} bytes")
print(f"Iterator over same data: {sys.getsizeof(large_iterator):,} bytes")
print(f"\n💡 Iterator is {sys.getsizeof(large_menu) // sys.getsizeof(large_iterator)}x smaller!")
print("   Because it doesn't store all items, just remembers position!")

# Example 8: Practical use case - Processing orders
print("\n" + "=" * 70)
print("🙋 Example 8: Real-World Use - Order Processing")
print("-" * 70)

class OrderQueue:
    """Iterator for processing customer orders"""
    
    def __init__(self, orders):
        self.orders = orders
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= len(self.orders):
            raise StopIteration
        
        order = self.orders[self.current]
        self.current += 1
        return order
    
    def orders_remaining(self):
        return len(self.orders) - self.current

# Simulate restaurant orders
today_orders = [
    "Table 1: Masala Dosa",
    "Table 2: Idli Vada Combo",
    "Table 3: Pongal",
    "Table 4: Filter Coffee"
]

print("Processing orders:")
order_queue = OrderQueue(today_orders)
for order_num, order in enumerate(order_queue, 1):
    print(f"  ✓ Served order #{order_num}: {order}")

# Example 9: Built-in iterators
print("\n" + "=" * 70)
print("🙋 Example 9: Python's Built-in Iterators")
print("-" * 70)

print("range() returns an iterator:")
r = range(1, 5)
print(f"range(1, 5): {r}")
print(f"Type: {type(r)}")
r_iter = iter(r)
print(f"First value: {next(r_iter)}")
print(f"Second value: {next(r_iter)}")

print("\nenumerate() returns an iterator:")
menu = ["Dosa", "Idli", "Vada"]
enum = enumerate(menu, start=1)
print(f"Type: {type(enum)}")
print(f"First: {next(enum)}")
print(f"Second: {next(enum)}")

print("\n" + "=" * 70)
print("✅ SUMMARY: Iterators")
print("=" * 70)
print("""
1. Iterator remembers its position during iteration
2. Has __iter__() and __next__() methods
3. Use next() to get items one by one
4. Raises StopIteration when exhausted
5. Can only iterate once (one-way traversal)
6. More memory efficient than storing all items
7. Think: Waiter serving orders one at a time
""")
