import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../0_data/PastHires.csv")

#Head row
print(df.head())
print()
# head row with 10 rows.
print(df.head(10))

# Tail end
print(df.tail(5))

# Shape of data: -> Dimensions.
print(df.shape) # -> rows, columns

# Size:
print(df.size) # rows * columns

#len -> nuymber of rows in the df.
print(len(df))

# columns:
print(df.columns)

## Extract some data:
print()
print(df["Hired"]) # Only this column returned.

# extract a range in the column.
print(df["Hired"][:5])
# Value on 5 row in hired column
print(df["Hired"][5])

# This data returned as a 1 dim array -> Series.

# You can extract more than 1 column. pass in array of column names
print()
print(df[["Years Experience", "Hired"]])
print()

## Ranges this way:
print(df[["Years Experience", "Hired"]][:5])

# Sorting ->
print(df.sort_values(["Years Experience"]))

# Value counts: Show the distribution for unqiue values in the data frame.
print()
degree_count = df["Level of Education"].value_counts()
print(degree_count)
print()

# Pandas is very simple of plotting the data too:
degree_count.plot(kind="bar") # Plotting using pandas.
plt.show()


###### Testing out pandas
# Columns:
# ['Years Experience', 'Employed?', 'Previous employers',
#        'Level of Education', 'Top-tier school', 'Interned', 'Hired']

prevEmp_Education_School = df[['Previous employers', 'Hired']][5:]
print(prevEmp_Education_School.value_counts())

prevEmp_Education_School.plot(kind="bar")
plt.show()