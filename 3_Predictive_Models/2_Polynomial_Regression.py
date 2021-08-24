import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)

pageSpeeds = np.random.normal(3,1,1000)
purchaseAmt = np.random.normal(50,10,1000) / pageSpeeds

plt.scatter(pageSpeeds, purchaseAmt)
plt.show()

#### X and Y Data arrays
x = np.array(pageSpeeds)
y = np.array(purchaseAmt)

p4 = np.poly1d(np.polyfit(x,y,4))

###########  Plotting
xp = np.linspace(0,7,100)
plt.scatter(x,y)
plt.plot(xp, p4(xp), c='r')
plt.show()


######## Getting the r2 score
from sklearn.metrics import r2_score
r2 = r2_score(y, p4(x))
print(r2)

