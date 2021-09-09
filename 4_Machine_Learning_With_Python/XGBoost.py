# Using XGBoost is easy.
# It's generally considered the best ML algorithm around right now.

from sklearn.datasets import load_iris

iris = load_iris()

numSamples, numFeatures = iris.data.shape
print(numSamples)
print(numFeatures)
print(list(iris.target_names))

#divide our data into 20% reserved for testing our model, and the remaining 80% to train it
# withholding our test data, we can make sure we're evaluating its results based on new flowers it hasn't seen before.

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)

#load up XGBoost, and convert our data into the DMatrix format it expects. One for the training data, and one for the test data.

import xgboost as xgb

train = xgb.DMatrix(X_train, label=y_train)
test = xgb.DMatrix(X_test, label=y_test)

# define our hyperparameters. We're choosing softmax since this is a multiple classification problem,
# but the other parameters should ideally be tuned through experimentation.

param = {
    'max_depth': 4,
    'eta': 0.3,
    'objective': 'multi:softmax',
    'num_class': 3}
epochs = 10

#  train our model using these parameters
model = xgb.train(param, train, epochs)

# use the trained model to predict classifications for the data we set aside for testing.
# Each classification number we get back corresponds to a specific species of Iris.

predictions = model.predict(test)
print("Predictions from Model: " , predictions)

# measure the accuracy on the test data
from sklearn.metrics import accuracy_score
print("Accuracy from Model: " , accuracy_score(y_test, predictions))



