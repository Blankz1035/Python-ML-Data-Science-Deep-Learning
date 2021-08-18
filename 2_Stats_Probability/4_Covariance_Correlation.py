import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def de_mean(x):
    xmean = np.mean(x)
    return [xi - xmean for xi in x]

def covariance(x,y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n-1)

pagespeeds = np.random.normal(3,1,1000)
purchaseamount = np.random.normal(50,10,1000)

plt.scatter(pagespeeds, purchaseamount)
plt.show()


purchaseamount = np.random.normal(50,10,1000) / pagespeeds
plt.scatter(pagespeeds, purchaseamount)
plt.show()

print("Covariance is: ", covariance(pagespeeds, purchaseamount))
print()

## Correlation values:
def correlation(x,y):
    stddevx = np.std(x)
    stddevy = np.std(y)
    return covariance(x,y) / stddevx / stddevy  ## check for 0 divisible... no need as we are just testing here.

print("Correlation is: ", correlation(pagespeeds, purchaseamount))


############ EASY WAY:
print("\nUsing just numpy,..")
print(np.corrcoef(pagespeeds, purchaseamount))


#### Create covariance using numpy using COV function. This is way simplier than coding. Useful library.