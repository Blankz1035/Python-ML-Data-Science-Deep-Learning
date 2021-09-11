# loading up the MovieLens dataset.
#  load the rows of the u.data and u.item files that we care about,
#  and merge them together so we can work with movie names instead of ID's.

import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('../0_data/ml/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('../0_data/ml/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

print(ratings.head())

# Now the amazing pivot_table function on a DataFrame will construct a user / movie rating matrix.
# Note how NaN indicates missing data - movies that specific users didn't rate.

movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print(movieRatings.head())

print()

# Let's extract a Series of users who rated Star Wars:
starWarsRatings = movieRatings['Star Wars (1977)']
print(starWarsRatings.head())

# Pandas' corrwith function to compute the pairwise correlation of Star Wars' vector of user rating
# with every other movie. After drop any results that have no data,
# and construct a new DataFrame of movies and their correlation score (similarity) to Star Wars

similarMovies = movieRatings.corrwith(starWarsRatings) # Create a vector with correlation of all movies.
similarMovies = similarMovies.dropna() # drop the NA values from the set.
df = pd.DataFrame(similarMovies) # create a dataframe from this data.
print(df.head(10)) # View the first 10 rows.

## Sort results:
print(similarMovies.sort_values(ascending=False))

## Results do not show anything of value. Movies shown may correlate, but have no relationship with star wars as a genre.


