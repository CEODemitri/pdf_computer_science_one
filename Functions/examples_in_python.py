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
# 5.2 :: Write a fucntion that scales an input x to its scientific notation scale so that 1 ≤ x ≤ 10. amount x is shifted should be stored in a pass by reference parameter. 
# ex. x = 314.15 should return 3.1415 and n = -2

# computer generated but not exactly what I need but a great reference 
# def scale_scientific(x, n):
#     if 1 <= x <= 10:
#         return x, n
#     else:
#         exponent = 0
#         while x >= 10:
#             x /= 10
#             exponent += 1
#         while x < 1:
#             x *= 10
#             exponent -= 1
#         return x, n + exponent

# print(scale_scientific(3.14))

# me generated
def scientific_scale(x):
    if 1 <= x <= 10:
        return x, 0
    else:
        scalar = 0
        while x >= 10:
            x /= 10
            scalar += 1
        while x < 1:
            x *= 10
            scalar -= 1
        return x, scalar
    
print(scientific_scale(400))


# 5.3 :: write a function that returns the most significant digit of a floating point number in the range 1 - 9 and 0 only if x = 0
# what is the most significant digit of a floating number? 
# after unnecessary research, seems to mean the biggest number

# x <- get input from user
# call function most_sig
# use boolean to check if number is 0
# if zero return number
# else use a [for loop?] to split the number into seperate numbers then add to an array? and return the first element in the array that is not a zero.


# 5.4 :: write a function that sums value of digits of given number 


# 5.5 :: write a function to convert radians to degrees with formula | deg = (180 * rad)/π |
# BONUS * convert degrees to radians


## 5.6 :: compute diameter, circumference and area of a circle given its radius. 
# **if support pass by reference, compute all three in one function

## 5.9 :: compute air distance between two locations given longitude and latitude


## 5.10 :: convert RGB color to CMYK 


## 5.11 convert rgb to a grayscale [three techniques-- luinosity, lightness, average methods]


## 5.13 compute a square root
def squared(x):
    absolute = abs(x)
    return absolute * absolute

print(squared(-5))
print(squared(-20))


# write a collection of functions that convert from: kilograms force, pounds, ounces, or Newtons
# 1 kgf = 2.20462 pounds
# 16 oz = 1 pound
# 1 kgf = 9.80665 Newtons


# 5.15 :: write a function that converts from: kilometer, mile, nautical mile and furlong
# 1 mile = 1.609347219 kilometers
# 1 nautical mile = 1.15078 miles
# 1 furlong = 1/8 mile



