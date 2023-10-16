import random
import tkinter as tk
import matplotlib
matplotlib.use("tkagg")
from matplotlib import pyplot

def visualize(sorting_algorithm, n):
    # Create array
    a = random.sample(range(1, n+1), n)
    
    # Generate sorting proccess
    sorting_process = sorting_algorithm(a)
    
    # Visualize sorting proccess
    while True:
        next_a, highlight1, highlight2, highlight3 = next(sorting_process, (None, None, None, None))
        
        if next_a is None:
            break
        else:
            bars = pyplot.bar(x=range(1, len(a) + 1), height=next_a)
            for h in highlight1:
                bars[h].set_color("red")
            for h in highlight2:
                bars[h].set_color("orange")
            for h in highlight3:
                bars[h].set_color("green")
            pyplot.axis("off")
            pyplot.pause(0.01)
            pyplot.clf()
            # print(next_step)

    bars = pyplot.bar(x=range(1, len(a) + 1), height=a)
    for b in bars:
        b.set_color("green")
    pyplot.axis("off")
    pyplot.show()
