# Python Iterables, Iterators & Generators

A comprehensive presentation explaining Python's iteration concepts using **Udupi Garden Restaurant** as a real-world analogy.

## 📚 Contents

### 🎯 Main Presentation
- **Python_Iterators_Generators.pptx** - 16-slide PowerPoint presentation with theory, code examples, and visualizations

### 💻 Interactive Demo Files
Run these Python files to see concepts in action:

1. **examples/01_iterable_demo.py** - Understanding Iterables
   - What makes something iterable
   - Common iterables (list, tuple, string, dict)
   - Multiple iteration passes
   - Memory usage

2. **examples/02_iterator_demo.py** - Understanding Iterators
   - Creating iterators with iter()
   - Using next() to get items
   - Custom iterator class
   - One-time traversal

3. **examples/03_generator_demo.py** - Understanding Generators
   - Generator functions with yield
   - Generator expressions
   - Memory efficiency (800x less!)
   - Infinite sequences
   - Real-world use cases

4. **examples/04_comparison_demo.py** - Side-by-side Comparison
   - All three concepts compared
   - Memory usage comparison
   - When to use each
   - Complete restaurant analogy

### 📊 Visualizations
- **visuals/memory_comparison.png** - Bar chart showing memory difference
- **visuals/restaurant_flow.png** - Customer → Waiter → Kitchen flow
- **visuals/iteration_comparison.png** - Visual comparison of all three
- **visuals/memory_scaling.png** - How memory scales with data size

### 📋 Data
- **examples/udupi_menu.py** - Complete Udupi Garden menu dataset

## 🚀 Quick Start

### Run All Demos
```bash
# Demo 1: Iterables
python3 examples/01_iterable_demo.py

# Demo 2: Iterators
python3 examples/02_iterator_demo.py

# Demo 3: Generators
python3 examples/03_generator_demo.py

# Demo 4: Comparison
python3 examples/04_comparison_demo.py
```

### View Menu Data
```bash
python3 examples/udupi_menu.py
```

### Regenerate Visualizations
```bash
python3 create_visualizations.py
```

### Regenerate Presentation
```bash
python3 create_presentation.py
```

## 🎓 Key Concepts

### The Restaurant Analogy

**🏪 UDUPI GARDEN RESTAURANT FLOW:**

1. **📋 MENU CARD (Iterable)**
   - Customer sees all dishes listed
   - Can read menu multiple times
   - All items visible at once

2. **🙋 WAITER (Iterator)**
   - Takes orders one by one
   - Remembers position (Table 1, 2, 3...)
   - Can't go backwards

3. **🍳 KITCHEN (Generator)**
   - Makes food ONLY when ordered
   - Doesn't prepare everything in advance
   - Most efficient - no waste!

### Memory Efficiency - The Key Takeaway

For **10,000 menu items**:
- **List (Iterable)**: 87,616 bytes (~85 KB)
- **Generator**: 104 bytes
- **Difference**: 842x LESS MEMORY! 🎉

This is why generators are crucial for:
- Processing large files
- Streaming data
- Infinite sequences
- Memory-constrained environments

## 📖 When to Use Each

### ✅ Use ITERABLE (List/Tuple)
- Small dataset that fits in memory
- Need multiple passes through data
- Need random access with indexing
- Example: Display menu categories

### ✅ Use ITERATOR
- Process items once sequentially
- Large dataset, don't need all in memory
- Example: Processing log files

### ✅ Use GENERATOR
- Very large or infinite sequences
- Memory efficiency is critical
- Items computed on-demand
- Example: Streaming data, huge files

## 🍽️ Udupi Garden Menu Items Used

The presentation uses authentic South Indian dishes:
- **Dosas**: Masala, Plain, Butter, Ghee, Rava, Onion, Mysore, Paneer, Set, Paper
- **Idlis**: Plain Idli, Set Idli
- **Vadas**: Medu Vada, Masala Vada
- **Uttapams**: Onion, Tomato Onion, Vegetable
- **Rice Items**: Sambhar Rice, Curd Rice, Pongal
- **Bread Items**: Puri, Chapati
- **Beverages**: Filter Coffee, Tea, Badam Milk

## 📋 Requirements

```bash
pip install python-pptx matplotlib pillow
```

## 🎬 Based On

This presentation is inspired by educational videos explaining Python iterators and generators using restaurant analogies, emphasizing the critical importance of memory efficiency in real-world applications.

## 📝 Features

- ✅ 16 comprehensive slides
- ✅ 4 interactive Python demos
- ✅ 4 visual charts and diagrams
- ✅ Real-world restaurant analogies
- ✅ Code examples with explanations
- ✅ Memory usage comparisons
- ✅ Beginner-friendly explanations
- ✅ Production-ready code

## 🎯 Learning Objectives

After going through this material, you will understand:
1. What makes an object iterable
2. How iterators work internally
3. The power of generators and lazy evaluation
4. When to use each approach
5. How to write memory-efficient Python code
6. The iterator protocol (__iter__ and __next__)
7. Generator expressions vs list comprehensions

## 🤝 Contributing

Feel free to improve the examples or add more use cases!

## 📄 License

Educational material - free to use and modify.

---

**Happy Learning! 🎉**

Remember: Generators are like efficient kitchens - they make food only when you order it!
