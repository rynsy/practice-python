from tkinter import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys
import random 
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg

WIDTH, HEIGHT = 800, 600
FIGURE_X, FIGURE_Y = 800, 600
BUCKET_RANGE = np.arange(0,10)
NUM_TESTS = 10000

def ordinator(key, mod):
    n = 0
    for l in key:
        n += ord(l)
    n %= mod
    return n

def random_words(n):
    words = []
    for _ in range(NUM_TESTS):
        w = []
        for _ in range(random.randint(5,20)):
            w.append(chr(random.randint(65,125)))
        words.append("".join(w))
    return words

def get_data(f, n):
    words = random_words(n)
    mod = max(BUCKET_RANGE) + 1
    data = {}
    for i in BUCKET_RANGE:
        data[i] = 0
    for w in words:
        data[ordinator(w, mod)] += 1
    return list(data.values())

def draw_figure(canvas, figure, loc=(0,0)):
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    return photo

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hash Function Distribution")
    canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
    canvas.pack()

    fig, ax = plt.subplots()
    ind = BUCKET_RANGE
    fig.figsize = (FIGURE_X, FIGURE_Y)
    data = get_data(ordinator, NUM_TESTS)
    bars = plt.bar(ind, data)

    ax.set_xticks(ind)
    ax.set_ylim([0, max(data)])
    ax.set_ylabel("Number of random words in bucket")

    fig_photo = draw_figure(canvas, fig, loc=(0,0))

    tk.mainloop()
    tk.destroy()
