import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

window = tk.Tk()

label = tk.Label(text='Distribution of Traffic Deaths in Memphis', width = 40, height = 40)
label.pack()


def graph():
    deaths= np.random.normal(35000,100,250)
    plt.hist(deaths, 50)
    plt.xlabel('Number of Deaths')
    plt.ylabel('Percentage of Deaths Caused by Traffic Accidents')
    plt.show()

button = tk.Button(text='Simulate', command=graph)
button.pack()


window.mainloop()
