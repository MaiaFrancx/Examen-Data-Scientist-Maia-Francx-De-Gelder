# Styling.py
import matplotlib.pyplot as plt

def set_style():
    # Turn off the grid
    plt.rcParams['axes.grid'] = False
    
    # Turn off the legend frame
    plt.rcParams['legend.frameon'] = False
    
    # Remove the upper and right frame lines
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    
    # Set the color scheme to blues, purples, and pinks
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#1f77b4', '#9467bd', '#e377c2'])
    
    # Additional customizations (optional)
    plt.rcParams['figure.figsize'] = [10, 6]
    plt.rcParams['lines.linewidth'] = 3
    plt.rcParams['font.size'] = 12

# Call the set_style function to apply the styles when the module is imported
set_style()
