import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

exit(0) ## Exit as 403 error on url request.

df = pd.read_excel('http://cdn.sundog-soft.com/udemy/datascience/cars.xls')

df1 = df[['Mileage','Price']]
bins = np.arange(0,50000,10000)
groups = df1.groupby(pd.cut(df1['Mileage'],bins)).mean()
print(groups.head())
groups['Price'].plot.line()

import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

x = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']

x[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(x[['Mileage', 'Cylinder', 'Doors']].values)

## Add a constant column to our model so we can have a Y intercept
print(x)

est = sm.OLS(y,x).fit()
print(est.summary())

##### Lets make an actual prediction for the data.
# checking if more doors means higher price
y.groupby(df.Doors).mean()

scaled = scale.transform([[45000,8,4]])
scaled = np.insert(scaled[0,0,1])  ## scaled array in format necessary, position 0, value of 1
print(scaled)
predicted = est.predict(scaled)
print(predicted)



