# KNN is a simple concept:
# define some distance metric between the items in your dataset, and find the K closest items.
# You can then use those items to predict some property of a test item, by having them somehow "vote" on
# it.
# In this example:
# try to guess the rating of a movie by looking at the 10 movies that are closest to it in terms of genres and popularity.

import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('../0_data/ml/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")
print("Ratings:\n", ratings.head())
print()
## Group by Movie ID and View Popularity (size):
import numpy as np
movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})
print("Movie Properties:\n", movieProperties.head())
print()
# The raw number of ratings isn't very useful for computing distances between movies, so we'll create a new DataFrame
# that contains the normalized number of ratings. So, a value of 0 means nobody rated it,
# and a value of 1 will mean it's the most popular movie there is

movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
print("Movie Normalized Num Ratings:\n", movieNormalizedNumRatings.head())

print()

# get the genre information from the u.item file. The way this works is there are 19 fields, each corresponding
# to a specific genre - a value of '0' means it is not in that genre, and '1' means it is in that genre.
# A movie may have more than one genre associated with it.

# dictionary called movieDict. Each entry will contain the movie name, list of genre values,
# the normalized popularity score, and the average rating for each movie


movieDict = {}
with open(r'../0_data/Ml/u.item', encoding="ISO-8859-1") as f:
    temp = ''
    for line in f:
        #line.decode("ISO-8859-1")
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, np.array(list(genres)), movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))

# example, here's the record we end up with for movie ID 1, "Toy Story"
print(movieDict[1])
print()

# let's define a function that computes the "distance" between two movies based on how similar
# their genres are, and how similar their popularity is.

from scipy import spatial


def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance

print("------------Computing Distance:-------------")
print("Distance of 2 and 4: ", ComputeDistance(movieDict[2], movieDict[4]))

# Note: Higher the distance, less compatible the movies are.
print(movieDict[2])
print(movieDict[4])

print()

# compute the distance between some given test movie (Toy Story, in this example) and all of the movies in our data set.
# When the sort those by distance, and print out the K nearest neighbors:

import operator


def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors


K = 10
avgRating = 0
neighbors = getNeighbors(1, K)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print(movieDict[neighbor][0] + " " + str(movieDict[neighbor][3]))

avgRating /= K

print()
# average rating of the 10 nearest neighbors to Toy Story:
print("Average Rating: ", avgRating)

# How does this compare to Toy Story's actual average rating?
print(movieDict[1])






