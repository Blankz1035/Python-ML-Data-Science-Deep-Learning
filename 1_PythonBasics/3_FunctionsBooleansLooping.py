def say_hello():
    print("Hello....")

# Specify parameter for import, and also a required datatype
def sqrnumber(x : int):
    return x*x

say_hello()
print(sqrnumber(5))

# Pass function as import parameter:
def do_something(f, x):
    return f(x)

print(do_something(sqrnumber, 5))

# Lamdas:
print(do_something(lambda  x: x*x*x, 3))

## Booleans
print("\nBooleans....")

## You can use english words for conditional statements. Indents are used to distiguish between logic functions
print(1==2)
print(1 is 2)
print(True or False)

if 1 > 2:
    print("Not True")
elif 1<2:
    print("True")
else:
    print("Middle!")


### Looping
print()
print("------Looping-----")

# range 10 means 0 - 9 .  Starting index is 0.
for x in range(10):
    print(x)

for x in range(10):
    if (x is 1):
        continue  # Move to next cycle
    if (x > 5):
        break  # Break from the loop cycle and move to next code
    print(x)

x = 0
while (x<10):
    print(x)
    x+=1


