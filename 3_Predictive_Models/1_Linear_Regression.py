import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

pageSpeeds = np.random.normal(3,1,1000)
purchaseAmt = 100 - (pageSpeeds + np.random.normal(0,1,1000)) * 3

plt.scatter(pageSpeeds, purchaseAmt)
plt.show()

## Line Regression on the data
slope, intercept, r_value, std_err = linregress(pageSpeeds, purchaseAmt)

print(r_value)
print()

##########
def predict(x):
    return slope * x + intercept


fitLine = predict(pageSpeeds)

plt.scatter(pageSpeeds, purchaseAmt)
plt.plot(pageSpeeds, fitLine, c='r')
plt.show()