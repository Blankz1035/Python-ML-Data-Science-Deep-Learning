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

















