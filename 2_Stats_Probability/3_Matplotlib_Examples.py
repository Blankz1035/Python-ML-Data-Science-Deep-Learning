## A great resource i found: https://towardsdatascience.com/clearing-the-confusion-once-and-for-all-fig-ax-plt-subplots-b122bb7783ca

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.arange(-3,3,0.001)

## Line on a graph
plt.plot(x, norm.pdf(x))
#plt.show()


## Multiple plots
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))  # mean of 1 and std of 0.5
#plt.show()


## Save to a file:
#plt.savefig('FilePath', format='png')

### Adjust the axes and personalize.
axs = plt.axes()
axs.set_xlim([-5,5])
axs.set_ylim([0,1.0])
axs.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axs.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
# plt.plot(x, norm.pdf(x))
# plt.plot(x, norm.pdf(x, 1.0, 0.5))
# plt.show()

# Easier way would be to use the arange in np to do this.

### Add a grid:
axs = plt.axes()
axs.set_xlim([-5,5])
axs.set_ylim([0,1.0])
axs.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axs.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
axs.grid()
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()

### Change the line type and colours.
# extra param on the plot function
axs = plt.axes()
axs.set_xlim([-5,5])
axs.set_ylim([0,1.0])
axs.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axs.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
axs.grid()
plt.plot(x, norm.pdf(x), 'b-')   # Blue and as a line
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r:') # Red and with vertical hashes
#plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r--') # Red and broken dash lines
#plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r-.') # Red and broken dots.
plt.show()


### Labeling Axes and Addin a legend value
axs = plt.axes()
axs.set_xlim([-5,5])
axs.set_ylim([0,1.0])
axs.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axs.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
axs.grid()
plt.xlabel("This is the X Axes")
plt.ylabel("This is the Y Axes")
plt.plot(x, norm.pdf(x), 'b-')   # Blue and as a line
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r:') # Red and with vertical hashes
plt.legend(['Xs', 'Os'], loc=4)   ## loc is the location as to where the legend is.
plt.show()

### xkcd=>  little easter egg to change the style to comic format! call on plt.xkcd()
### for Fun:
plt.xkcd()
fig, axs = plt.subplots()

axs.spines['right'].set_color('none')
axs.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
axs.set_ylim([-30,10])

data = np.ones(100)
data[70:] -= np.arange(30)

plt.annotate(
    "THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED",
    xy=(70,1), arrowprops=dict(arrowstyle='->'), xytext=(15,-10)
)

plt.plot(data)
plt.xlabel('time')
plt.ylabel('my overall health')

plt.show()

# Remove the mode:
plt.rcdefaults()

####################### PIE CHARTS
values = [12,55,4,32,14]
colors = ['r','g','b','c','m']
explode = [0,0,0.2,0,0]
labels = ['India','United States','Russia','China','Europe']
plt.pie(values, colors=colors, labels = labels, explode = explode)
plt.title("Location of Students")
plt.show()


########  Bar Charts
values = [12,55,4,32,14]
colors = ['r','g','b','c','m']
plt.bar(range(0,5), values, color = colors)
plt.show()

######  Scatter
x = np.random.rand(500)
y = np.random.rand(500)
plt.scatter(x,y)  # random 500  numbers Normal Distribution
plt.show()


####### Histogram
incomes = np.random.normal(27000,15000,10000)
plt.hist(incomes, 50)
plt.show()


### Box and Whisker plot:
# Box represents inner quartiles 50% of data resides and 25% represents above and below.
# We define dotted line (whiskers) that indicate the range of data except for outliers, which are plotted outside of the whiskers.
#Outliers are 1.5 X or more the interquartile range.

uniformskewed = np.random.rand(100) * 100 - 40
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(10) * -50 - 100
data = np.concatenate((uniformskewed, high_outliers, low_outliers))
plt.boxplot(data)
plt.show()