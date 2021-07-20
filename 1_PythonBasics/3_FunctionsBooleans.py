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

print(1==2)
print(1 is 2)
print(True or False)

if 1 > 2:
    print("Not True")
elif 1<2:
    print("True")
else:
    print("Middle!")
