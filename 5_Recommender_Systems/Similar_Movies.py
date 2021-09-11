# loading up the MovieLens dataset.
#  load the rows of the u.data and u.item files that we care about,
#  and merge them together so we can work with movie names instead of ID's.

import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('../0_data/ml/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('../0_data/ml/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

print("Ratings:\n", ratings.head())
print()

# Now the amazing pivot_table function on a DataFrame will construct a user / movie rating matrix.
# Note how NaN indicates missing data - movies that specific users didn't rate.

movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print("Moving Ratings:\n", movieRatings.head())

print()

# Let's extract a Series of users who rated Star Wars:
starWarsRatings = movieRatings['Star Wars (1977)']
print("Star Wars Ratings:\n", starWarsRatings.head())
print()

# Pandas' corrwith function to compute the pairwise correlation of Star Wars' vector of user rating
# with every other movie. After drop any results that have no data,
# and construct a new DataFrame of movies and their correlation score (similarity) to Star Wars

similarMovies = movieRatings.corrwith(starWarsRatings) # Create a vector with correlation of all movies.
similarMovies = similarMovies.dropna() # drop the NA values from the set.
df = pd.DataFrame(similarMovies) # create a dataframe from this data.
print("Similar Movie Preview (before sort)\n", df.head(10)) # View the first 10 rows.
print()

## Sort results:
print("Similar Movies Results:\n", similarMovies.sort_values(ascending=False))
print()

## Results do not show anything of value. Movies shown may correlate, but have no relationship with star wars as a genre.
print("----------------------------------")

# we need to get rid of movies that were only watched by a few people that are producing spurious results
# Let's construct a new DataFrame that counts up how many ratings exist for each movie, and also the average
# rating while we're at it.

import numpy as np
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
print("Movie Stats:\n", movieStats.head())
print()

# Let's get rid of any movies rated by fewer than X people,
# and check the top-rated ones that are left:
popularMovies = movieStats['rating']['size'] >= 100
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]

# Let's join this data with our original set of similar movies to Star Wars:
df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
# sort these new results by similarity score.
df = df.sort_values(['similarity'], ascending=False)[:15]
print("Final Recommendation:\n", df.head())


