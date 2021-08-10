#### Mean / Mode / Median / Variation / Standard Deviation
import numpy as np
import matplotlib.pyplot as plt

# Mean -> numpy has a function to do this.
incomes = np.random.normal(27000,15000,10000)
np.mean(incomes)

# Histogram of the data: (data ,  buckets)
plt.hist(incomes, 50)
plt.show()

# Median
np.median(incomes)

# Having outliers in your ds will cause a massive scew in the data. This is why you should always verify your data.

#### Mode:
ages = np.random.randint(18,high=90, size=500)
from scipy import stats
print(stats.mode(ages))


# Standard Deviation -> spread of data
