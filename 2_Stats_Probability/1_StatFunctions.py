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
import numpy as np
import matplotlib.pyplot as plt

# Mean -> numpy has a function to do this.
incomes = np.random.normal(100.0,20.0,10000)
np.mean(incomes)

# Histogram of the data: (data ,  buckets)
plt.hist(incomes, 50)
plt.show()

print(incomes.std())
print(incomes.var())


#### Data Distributions:
import numpy as np
import matplotlib.pyplot as plt

values = np.random.uniform(-10.0,10.0,100000)
plt.hist(values, 50)
plt.show()

## Gaussain / Normal visualization
from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.arange(-3,3,0.0001)
plt.plot(x, norm.pdf(x))
plt.show()
## Exponential PDF / Power Law
from scipy.stats import expon
import matplotlib.pyplot as plt

x = np.arange(0,10,0.0001)
plt.plot(x, expon.pdf(x))
plt.show()


## Binomial Probability Mass Function (discrete data)
from scipy.stats import binom
import matplotlib.pyplot as plt

x = np.arange(0,10,0.0001)
plt.plot(x, binom.pmf(x, 10,0.05))
plt.show()

## Poisson Probability Mass Function
from scipy.stats import poisson
import matplotlib.pyplot as plt

mu = 500
x = np.arange(400,600,0.5)
plt.plot(x, poisson.pmf(x, mu))
plt.show()

# Can use this example to see probability of a value happening outside of a range.





