"""
Create visualizations for the Python Iterables presentation
Generates charts and diagrams showing memory comparisons and flow diagrams
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrow
import numpy as np
import sys
import os

# Set up matplotlib to work without display
plt.switch_backend('Agg')

# Create output directory
os.makedirs('visuals', exist_ok=True)

def create_memory_comparison_chart():
    """Create bar chart comparing memory usage: List vs Generator"""
    print("Creating memory comparison chart...")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Data from the video reference (list vs generator memory usage)
    categories = ['List\n(10,000 items)', 'Generator\n(10,000 items)']
    memory_bytes = [87616, 104]  # Actual memory usage
    colors = ['#FF6B6B', '#4ECDC4']  # Red for list, Teal for generator
    
    bars = ax.bar(categories, memory_bytes, color=colors, alpha=0.8, edgecolor='black', linewidth=2)
    
    # Add value labels on bars
    for bar, value in zip(bars, memory_bytes):
        height = bar.get_height()
        if value > 10000:
            label = f'{value:,} bytes\n(~85 KB)'
        else:
            label = f'{value} bytes'
        ax.text(bar.get_x() + bar.get_width()/2., height,
                label, ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax.set_ylabel('Memory Usage (bytes)', fontsize=14, fontweight='bold')
    ax.set_title('Memory Comparison: List vs Generator\n(10,000 Dosa Orders)', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_ylim(0, max(memory_bytes) * 1.2)
    
    # Add annotation showing the difference
    ax.annotate('', xy=(1, memory_bytes[1] + 5000), xytext=(0, memory_bytes[0] - 5000),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax.text(0.5, memory_bytes[0]/2, '842x\nLess Memory!', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.8))
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('visuals/memory_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Memory comparison chart created: visuals/memory_comparison.png")

def create_restaurant_flow_diagram():
    """Create flow diagram showing Customer -> Waiter -> Kitchen flow"""
    print("Creating restaurant flow diagram...")
    
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4)
    ax.axis('off')
    
    # Colors matching South Indian theme
    customer_color = '#FFD93D'  # Yellow
    waiter_color = '#6BCB77'    # Green
    kitchen_color = '#FF6B6B'   # Red
    
    # Customer box
    customer_box = FancyBboxPatch((0.5, 1.5), 2, 1.5, 
                                   boxstyle="round,pad=0.1", 
                                   facecolor=customer_color, 
                                   edgecolor='black', linewidth=2)
    ax.add_patch(customer_box)
    ax.text(1.5, 2.25, '👤 Customer', ha='center', va='center', 
            fontsize=14, fontweight='bold')
    ax.text(1.5, 1.9, '(Iterable)', ha='center', va='center', fontsize=10, style='italic')
    
    # Arrow 1
    ax.annotate('', xy=(4, 2.25), xytext=(2.7, 2.25),
                arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax.text(3.35, 2.6, 'Orders', ha='center', fontsize=10, fontweight='bold')
    
    # Waiter box
    waiter_box = FancyBboxPatch((4, 1.5), 2, 1.5, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor=waiter_color, 
                                 edgecolor='black', linewidth=2)
    ax.add_patch(waiter_box)
    ax.text(5, 2.25, '🙋 Waiter', ha='center', va='center', 
            fontsize=14, fontweight='bold')
    ax.text(5, 1.9, '(Iterator)', ha='center', va='center', fontsize=10, style='italic')
    
    # Arrow 2
    ax.annotate('', xy=(7.5, 2.25), xytext=(6.2, 2.25),
                arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax.text(6.85, 2.6, 'One at a time', ha='center', fontsize=10, fontweight='bold')
    
    # Kitchen box
    kitchen_box = FancyBboxPatch((7.5, 1.5), 2, 1.5, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor=kitchen_color, 
                                  edgecolor='black', linewidth=2)
    ax.add_patch(kitchen_box)
    ax.text(8.5, 2.25, '🍳 Kitchen', ha='center', va='center', 
            fontsize=14, fontweight='bold')
    ax.text(8.5, 1.9, '(Generator)', ha='center', va='center', fontsize=10, style='italic')
    
    # Arrow 3 (back to customer)
    ax.annotate('', xy=(1.5, 1.3), xytext=(8.5, 1.3),
                arrowprops=dict(arrowstyle='->', lw=3, color='green', 
                               connectionstyle="arc3,rad=-.3"))
    ax.text(5, 0.5, '🍽️ Serves on-demand (yield)', ha='center', 
            fontsize=11, fontweight='bold', color='green')
    
    # Title
    ax.text(5, 3.6, 'Restaurant Ordering Flow: Iterable → Iterator → Generator', 
            ha='center', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('visuals/restaurant_flow.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Restaurant flow diagram created: visuals/restaurant_flow.png")

def create_iteration_comparison():
    """Create visual showing how iteration works for all three concepts"""
    print("Creating iteration comparison diagram...")
    
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    
    items = ['Idli', 'Dosa', 'Vada', 'Pongal']
    
    # Iterable (List)
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('ITERABLE (List)', fontsize=14, fontweight='bold', pad=10)
    
    y_pos = 8
    for i, item in enumerate(items):
        box = FancyBboxPatch((1, y_pos - i*1.5), 8, 1, 
                             boxstyle="round,pad=0.05", 
                             facecolor='#FFE66D', 
                             edgecolor='black', linewidth=1.5)
        ax.add_patch(box)
        ax.text(5, y_pos - i*1.5 + 0.5, f'"{item}"', 
                ha='center', va='center', fontsize=11, fontweight='bold')
    
    ax.text(5, 1, 'All items stored\nin memory', ha='center', 
            fontsize=10, style='italic', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    # Iterator
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('ITERATOR', fontsize=14, fontweight='bold', pad=10)
    
    y_pos = 8
    for i, item in enumerate(items):
        alpha = 0.3 if i > 0 else 1.0  # Only first item is highlighted
        box = FancyBboxPatch((1, y_pos - i*1.5), 8, 1, 
                             boxstyle="round,pad=0.05", 
                             facecolor='#6BCB77', 
                             edgecolor='black', linewidth=1.5, alpha=alpha)
        ax.add_patch(box)
        text_alpha = 0.4 if i > 0 else 1.0
        ax.text(5, y_pos - i*1.5 + 0.5, f'"{item}"', 
                ha='center', va='center', fontsize=11, fontweight='bold', alpha=text_alpha)
    
    # Add pointer arrow
    ax.annotate('', xy=(0.5, 8.5), xytext=(0.5, 9.5),
                arrowprops=dict(arrowstyle='->', lw=3, color='red'))
    ax.text(0.5, 9.8, '👆', ha='center', fontsize=16)
    
    ax.text(5, 1, 'Access one at a time\nwith next()', ha='center', 
            fontsize=10, style='italic', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    # Generator
    ax = axes[2]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('GENERATOR', fontsize=14, fontweight='bold', pad=10)
    
    # Show only the first item being "created"
    y_pos = 8
    box = FancyBboxPatch((1, y_pos), 8, 1, 
                         boxstyle="round,pad=0.05", 
                         facecolor='#4ECDC4', 
                         edgecolor='black', linewidth=2)
    ax.add_patch(box)
    ax.text(5, y_pos + 0.5, f'"{items[0]}"', 
            ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Show placeholder for rest
    for i in range(1, 4):
        ax.text(5, y_pos - i*1.5 + 0.5, '...', 
                ha='center', va='center', fontsize=16, color='gray')
    
    ax.text(5, 1.5, 'Items created on-demand\n(yield)', ha='center', 
            fontsize=10, style='italic', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    ax.text(5, 0.3, '💚 Memory Efficient!', ha='center', 
            fontsize=11, fontweight='bold', color='green')
    
    plt.tight_layout()
    plt.savefig('visuals/iteration_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Iteration comparison diagram created: visuals/iteration_comparison.png")

def create_memory_scaling_chart():
    """Create chart showing how memory scales with data size"""
    print("Creating memory scaling chart...")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Number of items
    sizes = np.array([100, 1000, 10000, 100000])
    
    # Approximate memory usage (bytes)
    list_memory = sizes * 8.76  # ~8.76 bytes per item for list
    generator_memory = np.full_like(sizes, 104, dtype=float)  # Constant ~104 bytes
    
    ax.plot(sizes, list_memory, 'o-', linewidth=3, markersize=10, 
            color='#FF6B6B', label='List (grows with size)')
    ax.plot(sizes, generator_memory, 's-', linewidth=3, markersize=10, 
            color='#4ECDC4', label='Generator (constant)')
    
    ax.set_xlabel('Number of Menu Items', fontsize=14, fontweight='bold')
    ax.set_ylabel('Memory Usage (bytes)', fontsize=14, fontweight='bold')
    ax.set_title('Memory Scaling: List vs Generator\n(Why Generators are Memory Efficient)', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12, loc='upper left')
    
    # Add annotations
    ax.annotate('Generator stays constant!\nOnly ~104 bytes', 
                xy=(100000, 104), xytext=(10000, 1000),
                arrowprops=dict(arrowstyle='->', color='green', lw=2),
                fontsize=11, fontweight='bold', color='green',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    ax.annotate('List grows linearly\nwith data size', 
                xy=(100000, list_memory[-1]), xytext=(50000, 100000),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=11, fontweight='bold', color='red',
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('visuals/memory_scaling.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Memory scaling chart created: visuals/memory_scaling.png")

def main():
    print("\n" + "="*60)
    print("CREATING VISUALIZATIONS FOR PRESENTATION")
    print("="*60 + "\n")
    
    create_memory_comparison_chart()
    create_restaurant_flow_diagram()
    create_iteration_comparison()
    create_memory_scaling_chart()
    
    print("\n" + "="*60)
    print("✓ ALL VISUALIZATIONS CREATED SUCCESSFULLY!")
    print("="*60)
    print("\nGenerated files in 'visuals/' directory:")
    print("  1. memory_comparison.png")
    print("  2. restaurant_flow.png")
    print("  3. iteration_comparison.png")
    print("  4. memory_scaling.png")
    print()

if __name__ == "__main__":
    main()
