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


