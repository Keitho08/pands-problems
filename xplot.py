# Keith Brazill (G00387845)
# 16th March 2020

# Write a program that displays a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np
import matplotlib.pyplot as plt

# x-axis values
x = np.arange(0.0, 4.0, 1.0) #x-axis values, range is 0.0 to 4.0 in steps of 1.0
# y-axis values
y1 = x      # f(x)
y2 = x**2   # g(x)
y3 = x**3   # h(x)

#plotting the points
plt.plot(y1, color='green', linestyle='solid', linewidth = 3, 
         marker='o', markerfacecolor='orange', markersize=6, label='f(x)') 
plt.plot(y2, color='blue', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='orange', markersize=6, label='g(x)') 
plt.plot(y3, color='red', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='orange', markersize=6, label='h(x)') 
# plots the point, line colour, linetype, linewidth, the marker on the line at point,
# colour of marker and marker size for each of above points (y1,y2 and y3),
# the label adds the name of the line, N.b plt.legend command is needed below 
# for this to work.

plt.xlabel('x-axis') # names xaxis "x-axis"
plt.ylabel('y-axis') # names yaxis "y-axis"

plt.title('f(x)[f(x)=x], g(x)[g(x)=x**2] and h(x)[h(x)=x**3]') # adds the plot title
plt.legend() # displays labels in plots above
plt.show() # Depicts graphic representation of the plot

# References
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# https://realpython.com/python-matplotlib-guide/
# https://stackoverflow.com/questions/17941083/how-to-label-a-line-in-matplotlib-python/17942066
# https://projects.datacamp.com/projects/33 (Datacamp Matplotlib tutorial)
# http://cs231n.github.io/python-numpy-tutorial/
# https://matplotlib.org/tutorials/introductory/pyplot.html
