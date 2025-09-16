# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

age= 42
height = 5.80
complex_number = 4 + 3j

# base_of_triangle = input("Enter base of triangle: ")
# height_of_triangle = input("Enter height of triangle: ")
# area_of_triangle = 0.5 * float(base_of_triangle) * float(height_of_triangle)
# print('The area of the triangle is ', area_of_triangle)

# side_a = input("Enter side a: ")
# side_b = input("Enter side b: ")
# side_c = input("Enter side c: ")
# perimeter_of_triangle = float(side_a) + float(side_b) + float(side_c)
# print('The perimeter of the triangle is ', perimeter_of_triangle)

# length  = input("Enter length of rectangle: ")
# width = input("Enter width of rectangle: ")
# area_of_rectangle = float(length) * float(width)
# perimeter_of_rectangle = 2 * (float(length) + float(width))
# print('The area of the rectangle is ', area_of_rectangle)
# print('The perimeter of the rectangle is ', perimeter_of_rectangle) 
# radius = input("Enter radius of a circle: ")
# area_of_circle = 3.14 * float(radius) ** 2
# circum_of_circle = 2 * 3.14 * float(radius)
# print('The area of the circle is ', area_of_circle)
# print('The circumference of the circle is ', circum_of_circle)      
# feet = input("Enter number of feet: ")
# meters = 0.3048 * float(feet)


# def calculateY(x):
#     y =2*x-2
#     return y

# def findSlope(x_1, x_2):
#     x1= x_1
#     y1=calculateY(x1)

#     x2= x_2
#     y2=calculateY(x2)
#     slope = (y2-y1)/(x2-x1)
#     print('The slope of the line is ', slope)

# findSlope(2,6)
print(len('python') > len('dragon'))   # False
print('on' in 'python' and 'on' in 'dragon') # True
print('jargon' in 'I hope this course is not full of jargon') # True
print('on' not in 'python' and 'on' in 'dragon') # False
print('jargon' not in 'I hope this course is not full of jargon') # False
print('on' in 'python' and 'on' in 'dragon') # True
print('on' not in 'python' and 'on' in 'dragon') # False

print( 'length of python and dragon is same: ', len('python') == len('dragon')) # True
length_of_python = len('python')
print(float((length_of_python))) # 6.0
length_of_dragon = len('dragon')
print(int((length_of_dragon)))   # 6

if int(length_of_python) == int(length_of_dragon):
    print('The length of python and dragon is same')
else:
    print('The length of python and dragon is not same')        
print('I hope this course is not full of jargon' .find('jargon')) # 31
print('Is int(7/3) == int(2.7)')
print("int(7/3) ", int(7/3))
print("int(2.7) ", int(2.7))
print(int(7/3) == int(2.7))

print('10' == 10) # False, because string is not equal to integer
print(int('10') == 10) # True, string 10 is converted to integer
print(float(9.8) == 10) # False, 9.8 is not equal to 10
print(int(9.8) == 10) # False, 9.8 is converted to 9
print(round(9.8) == 10) # True, 9.8 is rounded to 10