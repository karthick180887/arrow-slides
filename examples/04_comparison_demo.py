"""
Demo 4: Comparing Iterables, Iterators, and Generators
Side-by-side comparison to understand the differences
"""

import sys
from udupi_menu import UDUPI_MENU, ALL_ITEMS

print("=" * 80)
print("DEMO 4: ITERABLE vs ITERATOR vs GENERATOR - Complete Comparison")
print("=" * 80)

# Example 1: Basic Definitions
print("\n📚 Example 1: What Are They?")
print("-" * 80)

print("ITERABLE (Menu Card):")
print("  • Any object that can return an iterator")
print("  • Has __iter__() method")
print("  • Examples: list, tuple, string, dict")
print("  • Can iterate multiple times")
print("  • All data stored in memory")

print("\nITERATOR (Waiter):")
print("  • Object that remembers position")
print("  • Has __iter__() and __next__() methods")
print("  • Can iterate only once")
print("  • More memory efficient than storing all data")

print("\nGENERATOR (Kitchen):")
print("  • Special type of iterator")
print("  • Created with 'yield' keyword")
print("  • Lazily generates values on-demand")
print("  • Most memory efficient")
print("  • Perfect for large or infinite sequences")

# Example 2: Code Comparison
print("\n" + "=" * 80)
print("📚 Example 2: Creating Each Type")
print("-" * 80)

print("1️⃣  ITERABLE (List):")
menu_iterable = ["Masala Dosa", "Idli", "Vada", "Pongal"]
print(f"   Code: menu = ['Masala Dosa', 'Idli', 'Vada', 'Pongal']")
print(f"   Result: {menu_iterable}")
print(f"   Type: {type(menu_iterable)}")

print("\n2️⃣  ITERATOR (from iterable):")
menu_iterator = iter(menu_iterable)
print(f"   Code: menu_iter = iter(menu)")
print(f"   Result: {menu_iterator}")
print(f"   Type: {type(menu_iterator)}")

print("\n3️⃣  GENERATOR (function):")
def menu_generator():
    yield "Masala Dosa"
    yield "Idli"
    yield "Vada"
    yield "Pongal"

menu_gen = menu_generator()
print(f"   Code: def menu_generator(): yield 'Masala Dosa' ...")
print(f"   Result: {menu_gen}")
print(f"   Type: {type(menu_gen)}")

# Example 3: Accessing Elements
print("\n" + "=" * 80)
print("📚 Example 3: How to Access Elements")
print("-" * 80)

# Iterable
print("1️⃣  ITERABLE - Can use for loop, indexing:")
menu_list = ["Dosa", "Idli", "Vada"]
print(f"   menu[0] = {menu_list[0]}")
print(f"   menu[1] = {menu_list[1]}")
print(f"   len(menu) = {len(menu_list)}")

# Iterator
print("\n2️⃣  ITERATOR - Only next() or for loop:")
menu_iter = iter(["Dosa", "Idli", "Vada"])
print(f"   next(menu_iter) = {next(menu_iter)}")
print(f"   next(menu_iter) = {next(menu_iter)}")
print("   ❌ No indexing: menu_iter[0] would raise error")
print("   ❌ No len(): len(menu_iter) would raise error")

# Generator
print("\n3️⃣  GENERATOR - Only next() or for loop:")
def gen():
    yield "Dosa"
    yield "Idli"
    yield "Vada"

menu_gen = gen()
print(f"   next(menu_gen) = {next(menu_gen)}")
print(f"   next(menu_gen) = {next(menu_gen)}")
print("   ❌ No indexing or len()")

# Example 4: Multiple Iterations
print("\n" + "=" * 80)
print("📚 Example 4: Can You Iterate Multiple Times?")
print("-" * 80)

menu = ["Dosa", "Idli"]

print("1️⃣  ITERABLE - YES, iterate multiple times:")
for i in range(2):
    print(f"   Pass {i+1}:", end=" ")
    for item in menu:
        print(item, end=" ")
    print()

print("\n2️⃣  ITERATOR - NO, only once:")
menu_iter = iter(menu)
print("   Pass 1:", end=" ")
for item in menu_iter:
    print(item, end=" ")
print("\n   Pass 2:", end=" ")
for item in menu_iter:
    print(item, end=" ")
print("(exhausted!)")

print("\n3️⃣  GENERATOR - NO, only once:")
def gen():
    yield "Dosa"
    yield "Idli"

menu_gen = gen()
print("   Pass 1:", end=" ")
for item in menu_gen:
    print(item, end=" ")
print("\n   Pass 2:", end=" ")
for item in menu_gen:
    print(item, end=" ")
print("(exhausted!)")

# Example 5: Memory Comparison - THE KEY DIFFERENCE
print("\n" + "=" * 80)
print("📚 Example 5: MEMORY USAGE - The Most Important Difference!")
print("-" * 80)

count = 10000

# Create large dataset
print(f"Creating {count:,} menu items:\n")

# List (Iterable)
large_list = [f"Dosa #{i}" for i in range(count)]
list_size = sys.getsizeof(large_list)

# Iterator
large_iter = iter(large_list)
iter_size = sys.getsizeof(large_iter)

# Generator
def large_gen(n):
    for i in range(n):
        yield f"Dosa #{i}"

gen = large_gen(count)
gen_size = sys.getsizeof(gen)

print(f"1️⃣  ITERABLE (List):    {list_size:>10,} bytes (~{list_size//1024} KB)")
print(f"2️⃣  ITERATOR:           {iter_size:>10,} bytes")
print(f"3️⃣  GENERATOR:          {gen_size:>10,} bytes")

print(f"\n🎯 GENERATOR vs LIST: {list_size // gen_size}x LESS MEMORY!")
print(f"🎯 ITERATOR vs LIST:  {list_size // iter_size}x LESS MEMORY!")

print("\n💡 THIS IS WHY GENERATORS ARE IMPORTANT!")
print("   For 100,000 items: List = ~800KB, Generator = 200 bytes")
print("   For 1,000,000 items: List = ~8MB, Generator = 200 bytes")

# Example 6: When to Use Each
print("\n" + "=" * 80)
print("📚 Example 6: When to Use Each?")
print("-" * 80)

print("✅ USE ITERABLE (List/Tuple) when:")
print("   • Need to access items multiple times")
print("   • Need random access (indexing)")
print("   • Need to know length")
print("   • Small dataset that fits in memory")
print("   • Example: Menu categories to display")

print("\n✅ USE ITERATOR when:")
print("   • Process items once sequentially")
print("   • Large dataset - don't need all in memory")
print("   • Don't need indexing or length")
print("   • Example: Processing log files")

print("\n✅ USE GENERATOR when:")
print("   • Very large or infinite sequences")
print("   • Items computed on-demand")
print("   • Memory efficiency is critical")
print("   • Stream processing")
print("   • Example: Reading huge files, infinite streams")

# Example 7: Real Restaurant Scenario
print("\n" + "=" * 80)
print("📚 Example 7: Real Restaurant Scenario")
print("-" * 80)

print("Scenario: 1000 customers ordering dosas\n")

print("❌ BAD - Using List (All at once):")
print("   Chef makes 1000 dosas immediately")
print("   All sit on counter getting cold")
print("   Uses ~80KB memory")
print("   Wasteful if customers cancel orders")

print("\n✅ GOOD - Using Generator (On-demand):")
print("   Chef makes dosa only when customer orders")
print("   Always fresh and hot")
print("   Uses only ~100 bytes memory")
print("   No waste if customers cancel")

def serve_customers_with_generator(count):
    """Serve customers efficiently with generator"""
    for i in range(1, count + 1):
        yield f"Fresh Dosa for Customer #{i}"

print("\nServing first 5 customers:")
dosa_service = serve_customers_with_generator(1000)
for _ in range(5):
    print(f"   {next(dosa_service)}")
print(f"   ... 995 more waiting (will be made when needed)")

# Example 8: Performance Characteristics
print("\n" + "=" * 80)
print("📚 Example 8: Performance Characteristics Summary")
print("-" * 80)

comparison = """
┌─────────────────┬──────────────┬──────────────┬──────────────┐
│ Feature         │ ITERABLE     │ ITERATOR     │ GENERATOR    │
├─────────────────┼──────────────┼──────────────┼──────────────┤
│ Multiple passes │ ✅ Yes       │ ❌ No        │ ❌ No        │
│ Indexing [i]    │ ✅ Yes       │ ❌ No        │ ❌ No        │
│ len() function  │ ✅ Yes       │ ❌ No        │ ❌ No        │
│ Memory usage    │ 🔴 High      │ 🟡 Medium    │ 🟢 Low       │
│ Lazy evaluation │ ❌ No        │ ✅ Partial   │ ✅ Yes       │
│ Infinite seq.   │ ❌ No        │ ❌ No        │ ✅ Yes       │
│ Creation time   │ 🔴 Slow      │ 🟢 Fast      │ 🟢 Fast      │
│ Easy to create  │ ✅ Yes       │ 🟡 Medium    │ ✅ Yes       │
└─────────────────┴──────────────┴──────────────┴──────────────┘
"""
print(comparison)

# Example 9: Code Examples Side by Side
print("\n" + "=" * 80)
print("📚 Example 9: Quick Code Reference")
print("-" * 80)

print("""
Creating:
  Iterable:  menu = ["Dosa", "Idli", "Vada"]
  Iterator:  menu_iter = iter(menu)
  Generator: def gen(): yield "Dosa"

Accessing:
  Iterable:  menu[0], menu[1], len(menu)
  Iterator:  next(menu_iter)
  Generator: next(gen())

Checking:
  Iterable:  hasattr(obj, '__iter__')
  Iterator:  hasattr(obj, '__iter__') and hasattr(obj, '__next__')
  Generator: type(obj).__name__ == 'generator'
""")

# Example 10: The Udupi Garden Analogy Summary
print("\n" + "=" * 80)
print("📚 Example 10: The Complete Udupi Garden Analogy")
print("-" * 80)

print("""
🏪 UDUPI GARDEN RESTAURANT FLOW:

1. MENU CARD (Iterable)
   📋 Customer sees all dishes listed
   📋 Can read menu multiple times
   📋 All items visible at once
   
2. WAITER (Iterator)
   🙋 Takes orders one by one
   🙋 Remembers position (Table 1, 2, 3...)
   🙋 Can't go backwards
   
3. KITCHEN (Generator)
   🍳 Makes food ONLY when ordered
   🍳 Doesn't prepare everything in advance
   🍳 Most efficient - no waste!
   
Real-world efficiency:
- BAD: Kitchen makes 1000 dosas at opening (List)
- GOOD: Kitchen makes dosa when customer orders (Generator)
""")

print("\n" + "=" * 80)
print("✅ KEY TAKEAWAY")
print("=" * 80)
print("""
Choose based on your needs:

📦 ITERABLE (List): Small data, need multiple passes/indexing
   Example: Display menu categories

📮 ITERATOR: Process once, don't need all in memory
   Example: Process order queue

🎯 GENERATOR: Large data, on-demand, memory critical
   Example: Stream processing, infinite sequences

Remember the video's lesson:
  List = 87,616 bytes for 10,000 items
  Generator = 104 bytes for 10,000 items
  That's 842x LESS MEMORY! 🎉
""")
