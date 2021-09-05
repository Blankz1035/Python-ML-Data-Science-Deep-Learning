##### Building a spam classifier using Naive bayes

import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def readFiles(path):

    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n': ## Skip the header of the email as we dont need this information. Just the body
                    inBody = True
            f.close()
            message = '\\n'.join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)

data = DataFrame({'message': [], 'class': []})  # two columns -> message and class.

## Modify current directory to requirement. My data is stored in a different folder in this repo.
os.chdir("..")
abs_path_spam = (os.path.abspath(os.curdir) + "\\0_data\\emails\\spam").replace("\\", "/")
abs_path_ham = (os.path.abspath(os.curdir) + "\\0_data\\emails\\ham").replace("\\", "/")

### Load the data into the frame
data = data.append(dataFrameFromDirectory(abs_path_spam, 'spam'))
data = data.append(dataFrameFromDirectory(abs_path_ham, 'ham'))

print(data.head())
print("done")


############### MultinomailNB function. We Will use this to classify the data. Needs actual data, and the expected outcome.
# Countvectorizer will take all the values in message column and represent as numbers.

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

## Now we have our classifer.


### If you want to try this out, we can pass in additional new data. for this we need to pass in
## the same format as the original data. So the data needs to be vectorized first.
examples = ['Free Viagra now!!!', "Hi John, how about a game of golf tomorrow?"]
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
print(predictions)

