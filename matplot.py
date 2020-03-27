#!/bin/python3
# <<<<<<-------data visualization------->>>>>>
# if matplotlib module not installed in system then first install it.
# In jupyter !pip install matplotlib

import matplotlib.pyplot as plt
import time

# x = [-1, 2, 3, 3, 7, 13, 15]
# y = [-2, 4, 5, 5, 6, 15, 18]
x = ['Punjab', 'Mumbai', 'Rajasthan', 'Kerala', 'MP', 'UP']
y = ['Lalchok', 'Anderi', 'Jaipur', 'Dadar', 'Haweli', 'Sadargunj']
# loading matplotlib library/module
plt.xlabel("Distance")   # for x axis
plt.ylabel("Time")      # for y axis
#plt.plot(x,y)    # this will draw a line
plt.plot(x,y,label="State")      # to give labels 
plt.scatter(x,y,s=120,label="City",marker='*',color='red')    # to plot asterisk in x, y
plt.bar(x,y,label="Ratio of difference cities",color='green')   # to draw bar chart
plt.grid(color='black')    # this will draw grid in the graph
plt.legend()      # it will show label in the plot
plt.show()         # it will show graph
