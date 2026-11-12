"""
Create Python Iterables, Iterators & Generators PowerPoint Presentation
Complete presentation with Udupi Garden restaurant examples
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
import os

# Initialize presentation
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# Define color scheme (South Indian theme)
COLORS = {
    'title': RGBColor(255, 107, 107),      # Red
    'subtitle': RGBColor(78, 205, 196),     # Teal
    'accent1': RGBColor(255, 214, 61),      # Yellow
    'accent2': RGBColor(107, 203, 119),     # Green
    'text': RGBColor(50, 50, 50),           # Dark gray
    'code_bg': RGBColor(245, 245, 245),     # Light gray
}

def add_title_slide(prs, title, subtitle):
    """Add a title slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    
    # Add background color
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 250, 240)  # Light beige
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2), Inches(9), Inches(1.5))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(54)
    title_para.font.bold = True
    title_para.font.color.rgb = COLORS['title']
    title_para.alignment = PP_ALIGN.CENTER
    
    # Subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(3.8), Inches(9), Inches(1))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.text = subtitle
    subtitle_para = subtitle_frame.paragraphs[0]
    subtitle_para.font.size = Pt(32)
    subtitle_para.font.color.rgb = COLORS['subtitle']
    subtitle_para.alignment = PP_ALIGN.CENTER
    
    # Footer
    footer_box = slide.shapes.add_textbox(Inches(0.5), Inches(6.5), Inches(9), Inches(0.5))
    footer_frame = footer_box.text_frame
    footer_frame.text = "With Real-World Udupi Garden Restaurant Examples"
    footer_para = footer_frame.paragraphs[0]
    footer_para.font.size = Pt(16)
    footer_para.font.italic = True
    footer_para.alignment = PP_ALIGN.CENTER

def add_content_slide(prs, title, content_items, add_image=None):
    """Add a content slide with bullet points"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(36)
    title_para.font.bold = True
    title_para.font.color.rgb = COLORS['title']
    
    # Content
    content_top = Inches(1.3)
    content_height = Inches(5.5) if not add_image else Inches(5.2)
    
    content_box = slide.shapes.add_textbox(
        Inches(0.5), content_top, 
        Inches(8.5) if not add_image else Inches(5), 
        content_height
    )
    text_frame = content_box.text_frame
    text_frame.word_wrap = True
    
    for i, item in enumerate(content_items):
        if i > 0:
            text_frame.add_paragraph()
        p = text_frame.paragraphs[i]
        p.text = item
        p.font.size = Pt(18)
        p.font.color.rgb = COLORS['text']
        p.level = 0
        p.space_after = Pt(8)
    
    # Add image if provided
    if add_image and os.path.exists(add_image):
        slide.shapes.add_picture(add_image, Inches(5.8), Inches(1.5), width=Inches(3.7))

def add_code_slide(prs, title, code_text, explanation):
    """Add a slide with code example"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.7))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(32)
    title_para.font.bold = True
    title_para.font.color.rgb = COLORS['title']
    
    # Code box with background
    code_shape = slide.shapes.add_shape(
        1,  # Rectangle
        Inches(0.5), Inches(1.2), Inches(9), Inches(3.5)
    )
    code_shape.fill.solid()
    code_shape.fill.fore_color.rgb = COLORS['code_bg']
    code_shape.line.color.rgb = RGBColor(200, 200, 200)
    
    # Code text
    code_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.4), Inches(8.6), Inches(3.1))
    code_frame = code_box.text_frame
    code_frame.text = code_text
    code_frame.word_wrap = False
    for para in code_frame.paragraphs:
        para.font.name = 'Courier New'
        para.font.size = Pt(14)
        para.font.color.rgb = RGBColor(0, 0, 0)
    
    # Explanation
    exp_box = slide.shapes.add_textbox(Inches(0.5), Inches(5), Inches(9), Inches(2))
    exp_frame = exp_box.text_frame
    exp_frame.text = explanation
    exp_frame.word_wrap = True
    for para in exp_frame.paragraphs:
        para.font.size = Pt(16)
        para.font.color.rgb = COLORS['text']

print("Creating presentation...")
print("="*70)

# Slide 1: Title
print("Creating Slide 1: Title")
add_title_slide(
    prs,
    "Python Iterables, Iterators & Generators",
    "Explained with Udupi Garden Menu"
)

# Slide 2: Introduction
print("Creating Slide 2: Introduction")
content = [
    "🏪 Imagine you're at Udupi Garden Restaurant...",
    "",
    "Question: How does the restaurant serve 100 customers efficiently?",
    "",
    "❌ BAD: Make all 100 meals at once → Cold food, wasted memory",
    "✅ GOOD: Make meals when ordered → Fresh food, efficient!",
    "",
    "This is exactly how Python generators work!",
    "Let's understand the three concepts:",
    "  • Iterable (Menu Card) - See all options",
    "  • Iterator (Waiter) - Order one by one",
    "  • Generator (Kitchen) - Cook on-demand"
]
add_content_slide(prs, "The Restaurant Analogy", content, "visuals/restaurant_flow.png")

# Slide 3: What is an Iterable?
print("Creating Slide 3: Iterable Concept")
content = [
    "📋 ITERABLE = The Menu Card",
    "",
    "Definition:",
    "  • Any object that can return an iterator",
    "  • Has __iter__() method",
    "",
    "Examples:",
    "  • Lists: ['Masala Dosa', 'Idli', 'Vada']",
    "  • Tuples: ('Dosa', 'Coffee')",
    "  • Strings: 'UDUPI'",
    "  • Dictionaries: {'breakfast': 'Idli', 'lunch': 'Thali'}",
    "",
    "Key Features:",
    "  ✓ Can iterate multiple times",
    "  ✓ All items stored in memory",
    "  ✓ Supports len() and indexing"
]
add_content_slide(prs, "What is an Iterable?", content)

# Slide 4: Iterable Code Example
print("Creating Slide 4: Iterable Code")
code = """# Udupi Garden Menu (Iterable)
menu = ["Masala Dosa", "Plain Dosa", "Idli", "Vada", "Pongal"]

# You can iterate multiple times
for item in menu:
    print(item)

# Supports indexing
print(menu[0])  # "Masala Dosa"

# Has length
print(len(menu))  # 5

# Check if iterable
print(hasattr(menu, '__iter__'))  # True"""

explanation = "💡 Like a menu card - you can read it again and again, see all items at once!"
add_code_slide(prs, "Iterable: Code Example", code, explanation)

# Slide 5: What is an Iterator?
print("Creating Slide 5: Iterator Concept")
content = [
    "🙋 ITERATOR = The Waiter",
    "",
    "Definition:",
    "  • Object that remembers its position",
    "  • Has __iter__() AND __next__() methods",
    "",
    "How it works:",
    "  1. Create iterator: menu_iter = iter(menu)",
    "  2. Get next item: next(menu_iter)",
    "  3. Raises StopIteration when exhausted",
    "",
    "Key Features:",
    "  ✓ One-way traversal (can't go back)",
    "  ✓ Can iterate only once",
    "  ✗ No indexing or len()",
    "  ✓ More memory efficient than storing all data",
    "",
    "Think: Waiter taking orders one at a time, can't go backwards!"
]
add_content_slide(prs, "What is an Iterator?", content)

# Slide 6: Iterator Code Example
print("Creating Slide 6: Iterator Code")
code = """# Creating iterator from menu
menu = ["Masala Dosa", "Idli", "Vada"]
menu_iterator = iter(menu)

# Getting items one by one
print(next(menu_iterator))  # "Masala Dosa"
print(next(menu_iterator))  # "Idli"
print(next(menu_iterator))  # "Vada"

# What happens next?
print(next(menu_iterator))  # Raises StopIteration!

# Can iterate only once
for item in menu_iterator:  # Nothing happens (exhausted)
    print(item)"""

explanation = "💡 Like a waiter - remembers position, serves one order at a time, can't repeat!"
add_code_slide(prs, "Iterator: Code Example", code, explanation)

# Slide 7: Custom Iterator Class
print("Creating Slide 7: Custom Iterator")
code = """class UdupiMenuIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item

# Usage
menu = UdupiMenuIterator(["Dosa", "Idli", "Vada"])
print(next(menu))  # "Dosa"
print(next(menu))  # "Idli\""""

explanation = "💡 Custom iterator with __iter__() and __next__() methods"
add_code_slide(prs, "Custom Iterator Class", code, explanation)

# Slide 8: What is a Generator?
print("Creating Slide 8: Generator Concept")
content = [
    "🍳 GENERATOR = The Kitchen",
    "",
    "Definition:",
    "  • Special iterator created with 'yield' keyword",
    "  • Generates values on-demand (lazy evaluation)",
    "",
    "How it works:",
    "  • Function pauses at 'yield'",
    "  • Resumes when next() is called",
    "  • State is maintained between calls",
    "",
    "Key Benefits:",
    "  ⭐ EXTREMELY memory efficient",
    "  ⭐ Perfect for large or infinite sequences",
    "  ⭐ Values computed only when needed",
    "  ✓ Lazy evaluation",
    "",
    "Think: Kitchen making food ONLY when customer orders!"
]
add_content_slide(prs, "What is a Generator?", content)

# Slide 9: Generator Function Example
print("Creating Slide 9: Generator Code")
code = """def serve_menu_items():
    print("Making Dosa...")
    yield "Masala Dosa"
    
    print("Making Idli...")
    yield "Idli"
    
    print("Making Coffee...")
    yield "Filter Coffee"

# Create generator
kitchen = serve_menu_items()

# Get items on-demand
print(next(kitchen))  # Prints "Making Dosa..." then "Masala Dosa"
print(next(kitchen))  # Prints "Making Idli..." then "Idli"
print(next(kitchen))  # Prints "Making Coffee..." then "Filter Coffee\""""

explanation = "💡 Function pauses at yield, resumes when next() called - items made on-demand!"
add_code_slide(prs, "Generator: Code Example", code, explanation)

# Slide 10: Generator Expression
print("Creating Slide 10: Generator Expression")
code = """# List comprehension (creates full list)
menu = ["DOSA", "IDLI", "VADA"]
lowercase_list = [item.lower() for item in menu]
print(lowercase_list)  # ['dosa', 'idli', 'vada']

# Generator expression (parentheses instead of brackets)
lowercase_gen = (item.lower() for item in menu)
print(lowercase_gen)  # <generator object>

# Get items on-demand
print(next(lowercase_gen))  # 'dosa'
print(next(lowercase_gen))  # 'idli'

# Memory comparison
import sys
print(sys.getsizeof(lowercase_list))  # ~120 bytes
print(sys.getsizeof(lowercase_gen))   # ~104 bytes"""

explanation = "💡 Generator expression: () instead of [] - creates generator, not list!"
add_code_slide(prs, "Generator Expression", code, explanation)

# Slide 11: Memory Comparison - THE KEY POINT
print("Creating Slide 11: Memory Comparison")
slide = prs.slides.add_slide(prs.slide_layouts[6])

# Title
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.7))
title_frame = title_box.text_frame
title_frame.text = "Memory Comparison: THE KEY DIFFERENCE!"
title_para = title_frame.paragraphs[0]
title_para.font.size = Pt(32)
title_para.font.bold = True
title_para.font.color.rgb = COLORS['title']

# Add memory comparison image
if os.path.exists('visuals/memory_comparison.png'):
    slide.shapes.add_picture('visuals/memory_comparison.png', Inches(0.5), Inches(1.2), width=Inches(9))

# Slide 12: Advanced Generator - Combos
print("Creating Slide 12: Advanced Generator")
code = """def generate_combos():
    dosas = ["Masala Dosa", "Plain Dosa", "Rava Dosa"]
    drinks = ["Filter Coffee", "Tea"]
    
    for dosa in dosas:
        for drink in drinks:
            yield f"{dosa} + {drink}"

# Generate meal combinations
combos = generate_combos()
print(next(combos))  # "Masala Dosa + Filter Coffee"
print(next(combos))  # "Masala Dosa + Tea"
print(next(combos))  # "Plain Dosa + Filter Coffee"
# ... and so on

# Infinite generator
def infinite_orders():
    num = 1
    while True:
        yield f"Order #{num}: Masala Dosa"
        num += 1"""

explanation = "💡 Generators can create combinations and infinite sequences efficiently!"
add_code_slide(prs, "Advanced: Combos & Infinite Sequences", code, explanation)

# Slide 13: Memory Visualization
print("Creating Slide 13: Memory Scaling")
slide = prs.slides.add_slide(prs.slide_layouts[6])

# Title
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.7))
title_frame = title_box.text_frame
title_frame.text = "Memory Scaling: Why Generators Win"
title_para = title_frame.paragraphs[0]
title_para.font.size = Pt(32)
title_para.font.bold = True
title_para.font.color.rgb = COLORS['title']

# Add scaling image
if os.path.exists('visuals/memory_scaling.png'):
    slide.shapes.add_picture('visuals/memory_scaling.png', Inches(0.5), Inches(1.2), width=Inches(9))

# Slide 14: When to Use Each
print("Creating Slide 14: When to Use")
content = [
    "Decision Guide:",
    "",
    "✅ Use ITERABLE (List/Tuple) when:",
    "  • Small dataset that fits in memory",
    "  • Need multiple passes through data",
    "  • Need random access with indexing",
    "  • Example: Display menu categories",
    "",
    "✅ Use ITERATOR when:",
    "  • Process items once sequentially",
    "  • Large dataset, don't need all in memory",
    "  • Example: Processing log files",
    "",
    "✅ Use GENERATOR when:",
    "  • Very large or infinite sequences",
    "  • Memory efficiency is critical",
    "  • Items computed on-demand",
    "  • Example: Streaming data, huge files"
]
add_content_slide(prs, "When to Use Each?", content, "visuals/iteration_comparison.png")

# Slide 15: Practical Use Cases
print("Creating Slide 15: Use Cases")
content = [
    "Real-World Applications:",
    "",
    "🏪 Restaurant Scenarios:",
    "  • Menu categories → Iterable (display all)",
    "  • Order queue → Iterator (process once)",
    "  • Daily specials → Generator (create on-demand)",
    "",
    "💻 Python Applications:",
    "  • Reading huge files → Generator",
    "  • Streaming data → Generator",
    "  • Processing logs → Iterator",
    "  • Database cursors → Iterator",
    "  • Infinite sequences → Generator",
    "",
    "Example: Reading 1GB file",
    "  ❌ list: Loads all 1GB into memory",
    "  ✅ generator: Reads one line at a time"
]
add_content_slide(prs, "Practical Use Cases", content)

# Slide 16: Summary
print("Creating Slide 16: Summary")
content = [
    "🎯 Key Takeaways:",
    "",
    "📋 ITERABLE (Menu Card)",
    "  • All items visible, can read multiple times",
    "  • Uses more memory, but supports indexing",
    "",
    "🙋 ITERATOR (Waiter)",
    "  • Access items one at a time, remembers position",
    "  • One-way traversal, more memory efficient",
    "",
    "🍳 GENERATOR (Kitchen)",
    "  • Creates items on-demand with 'yield'",
    "  • MOST memory efficient (100-800x less!)",
    "  • Perfect for large data and infinite sequences",
    "",
    "Remember: List = 87KB, Generator = 104 bytes for 10,000 items!",
    "",
    "Practice with the demo files: examples/*.py"
]
add_content_slide(prs, "Summary & Key Takeaways", content)

# Save presentation
output_file = "Python_Iterators_Generators.pptx"
prs.save(output_file)

print("="*70)
print(f"✅ Presentation created successfully: {output_file}")
print(f"   Total slides: {len(prs.slides)}")
print("="*70)
