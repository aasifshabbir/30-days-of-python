# Introduction
# Day 1 - 30DaysOfPython Challenge

print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool

# ecludian the print statement
print('Hello, World!')  # Print a string
print('Welcome to 30DaysOfPython Challenge!')  # Print a welcome message

# euclidean distance
x1, y1 = 2, 3
x2, y2 = 10, 8
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f'The Euclidean distance between points ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}')
