# PCA is a dimensionality reduction technique:
# it lets you distill multi-dimensional data down to fewer dimensions,
# selecting new dimensions that preserve variance in the data as best it can

# Example using IRIS dataset. This DS has a total of 4 dimensions.
# We will do PCA on this to transform the DS into a lower dimension ratio and review the results.

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle

## Load the DS using import
iris = load_iris()

## shape returns a tuple of the size of the dataset and the number of features -> dimensions.
numSamples, numFeatures = iris.data.shape
print(numSamples)
print(numFeatures)
print(list(iris.target_names))
print()


X = iris.data
pca = PCA(n_components=2, whiten=True).fit(X) # n_component will represent the dimensions we want to tranform.
# Whiten will normalize all the data
X_pca = pca.transform(X)

print("PCA Components: \n", pca.components_)
print()

print("Explained Variance:")
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))
print()
# PCA will optimize and choose the best dimensionality to preserve the data.


from pylab import *
colors = cycle('rgb')
target_ids = range(len(iris.target_names))
pl.figure()
for i, c, label in zip(target_ids, colors, iris.target_names):
    pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1],
        c=c, label=label)
pl.legend()
pl.show()

