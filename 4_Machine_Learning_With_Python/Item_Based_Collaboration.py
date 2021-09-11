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

userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print("User Ratings:\n", userRatings.head())

