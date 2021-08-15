# Percentiles:
# 	- In a data set whats the point at which x% of the values are less than that value.
# 	- Example income distribution.
# 	- 99th percentile is the people making less than the amount.
#
# Also used in terms of quartiles in a distribution. This is points that contain 50% of the data.
#
#
#
#
# Moments:
# Quantitative measures of the shape of a prob den function.
# Mathematically, they are a bit hard to wrap the head around.
#
# The first moment is the Mean.
# Second is the variance.
# Third moment is called Skey -> measure of how lop sided the distribution is.  A negative skey has a long tail on the left.
# The fourth moment is called Kurtosis. This is how think the tail is and how sharp the peak is compared to normal distribution.



### Percentiles

import numpy as np
import matplotlib.pyplot as plt

values = np.random.normal(100.0,20.0,10000)
plt.hist(values, 50)
plt.show()

print("Percentiles")
print(np.percentile(values, 50))
print(np.percentile(values, 90))
print(np.percentile(values, 30))

print()

#### Moments:
import scipy.stats as sp
print("Moments")
print(np.mean(values))
print(np.var(values))
print(sp.skew(values))
print(sp.kurtosis(values))
