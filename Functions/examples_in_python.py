# A function is a sequence of instructions packaged into a unit that can be reused
# a function performs a specific task

# basic function
def greet(name = "World"):
    print ("Hello " + name)

greet("Hannah")


def upperCase(string):
    return string.upper()

print(upperCase("hello"))


# Exercises
# 5.2 ::Write a fucntion that scales an input x to its scientific notation scale so that 1 ≤ x ≤ 10. amount x is shifted should be stored in a pass by reference parameter. 
# ex. x = 314.15 should return 3.1415 and n = -2
