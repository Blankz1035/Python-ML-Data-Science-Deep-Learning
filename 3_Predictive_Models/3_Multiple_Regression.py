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




