# Program to demonstrate some features of lits

x = [1,2,3,4,5,6]

#length of List
print(len(x))

#index of list
print(x[3])

#Slice of list
print(x[:3])
print(x[3:])
print(x[-2:])

# Extending List
print(x.extend([7,8]))
print(x.append(9))

#List of Lists
y = [1,2,3]
listoflists = [x,y]
print(listoflists)

# Sorting
print(x.sort(reverse=True))
print(x.sort())

print("\nTuples....")
#imutable lists -> use () instead of []

x = (1,2,3)
y = (4,5,6)
listOfTuples = [x,y]
print(listOfTuples)

# Create a tuple
(age, income) = "32,30000".split(",")
print(age)
print(income)

# Dictionaries
print("\nDictionaries...")

newdictionary = dict({"key1" : 1, "key2" : 2, "key3" : 3})
print(newdictionary)

# Access a value by using the key:
print(newdictionary["key1"])
print(newdictionary.values()) # print values from the dictionary
print(newdictionary.keys()) # print keys from the dictionary
