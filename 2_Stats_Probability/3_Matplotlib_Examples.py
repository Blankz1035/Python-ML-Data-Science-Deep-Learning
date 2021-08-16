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


