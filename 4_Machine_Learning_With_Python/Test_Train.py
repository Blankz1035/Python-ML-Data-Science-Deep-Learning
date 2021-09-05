import numpy as np
import matplotlib.pyplot as plt

pageSpeeds = np.random.normal(3.0,1.0,100)
purchaseAmounts = np.random.normal(50.0,30.0,100) / pageSpeeds

plt.scatter(pageSpeeds, purchaseAmounts)
#plt.show()
### Splitting the data to train  / test.  We will split 80 / 20.
# Note as the original data is randomized, we do not need to shuffle the data. However you will need to do this for
## real world data.
# Pandas can also split data for you, as well as scilkit learn

trainx = pageSpeeds[:80]
testx = pageSpeeds[80:]

trainy = purchaseAmounts[:80]
testy = purchaseAmounts[80:]

plt.scatter(trainx, trainy)
#plt.show()

plt.scatter(testx, testy)
#plt.show()

###################### Polynomials -> trying to find the best degree for overfitting.
x = np.array(trainx)
y = np.array(trainy)

p4 = np.poly1d(np.polyfit(x,y,3))

### Now we want to plot the polynomail against the training data
xp = np.linspace(0,7,100)
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])
plt.scatter(x,y)
plt.plot(xp, p4(xp), c='r')
plt.show()

## Now against our test data:
testtx = np.array(testx)
testty = np.array(testy)

axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])
plt.scatter(testtx,testty)
plt.plot(xp, p4(xp), c='r')
plt.show()


##### Accuracy:  R_2
from sklearn.metrics import r2_score
r2 = r2_score(testty, p4(testtx))
print(r2)

r2 = r2_score(np.array(trainy), p4(np.array(trainx)))
print(r2)
