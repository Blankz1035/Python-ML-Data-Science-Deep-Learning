# loading up the MovieLens dataset.
#  load the rows of the u.data and u.item files that we care about,
#  and merge them together so we can work with movie names instead of ID's.

import pandas as pd

### Function for reuseability
def DisplayUserRecommendations(userID: int):
    # Now let's produce some movie recommendations for user ID 0
    myRatings = userRatings.loc[userID].dropna()
    myRatings

    if myRatings.empty:
        print("Invalid User")
    else:
        # let's go through each movie rated one at a time, and build up a list of possible
        # recommendations based on the movies similar to the ones rated.
        print("Beginning Similar Movie Checks...\n")
        simCandidates = pd.Series()
        for i in range(0, len(myRatings.index)):
            print("Adding sims for " + myRatings.index[i] + "...")
            # Retrieve similar movies to this one that I rated
            sims = corrMatrix[myRatings.index[i]].dropna()
            # Now scale its similarity by how well I rated this movie
            sims = sims.map(lambda x: x * myRatings[i])
            # Add the score to the list of similarity candidates
            simCandidates = simCandidates.append(sims)

        print()
        # Glance at our results so far:
        print("sorting...\n")
        simCandidates.sort_values(inplace=True, ascending=False)
        print(simCandidates.head(10))
        print()
        # Note that some of the same movies came up more than once, because they were similar to more than one movie rated.
        # We'll use groupby() to add together the scores from movies that show up more than once.
        print("Similar Candidates (Grouped)...\n")
        simCandidates = simCandidates.groupby(simCandidates.index).sum()
        simCandidates.sort_values(inplace=True, ascending=False)
        simCandidates.head(10)
        print()

        # Last thing we have to do is filter out movies already rated, as recommending a seen movie is not good.
        print("Filtered Results...\n")
        filteredSims = simCandidates.drop(myRatings.index)
        filteredSims.head(10)


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

# pandas has a built-in corr() method that will compute a correlation score for every column
# pair in the matrix
# This gives us a correlation score between every pair of movies
# (where at least one user rated both movies, otherwise nan will show).

corrMatrix = userRatings.corr()
corrMatrix.head()

# avoid spurious results that happened from just a handful of users
# that happened to rate the same pair of movies
# In order to restrict our results to movies that lots of people rated together - and also give us more popular
# that are more easily recongnizable - we'll use the min_periods argument to throw out results
# where fewer than 100 users rated a given movie pair

print("User Rating Correlation with Minimum amount of ratings...\n")
corrMatrix = userRatings.corr(method='pearson', min_periods=100)
corrMatrix.head()

### User Input

print("Welcome to the Movie recommendations.")
choice = 0
while (choice != 7):

    try:
        choice = int(input("Enter a User ID to view recommendations: "))

        ## Call function and display details.
        DisplayUserRecommendations(choice)

    except:
        print("Invalid Value.")
        print()

print("Done")









