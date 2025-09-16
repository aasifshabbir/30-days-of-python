
# Variables in Python
print('Day 2: 30 Days of python programming')
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print(type(skills))
print('---')
print('Skills: ', skills)
print(type(person_info))
print
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True
Player_name, team, position, age, is_active = 'Lionel Messi', 'PSG', 'Forward', 35, True
print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
print('Player name:', Player_name)
print('Team:', team)
print('Position:', position)
print('Age:', age)
print('Is active:', is_active)
print('---')
# Unpacking a collection
print(len(Player_name))
if len(Player_name) > len(first_name):
    print(f'{Player_name} is longer than {first_name}')
else:
    print(f'{first_name} is longer than {Player_name}') 

num_one =5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two

def calculate_area_of_circle(r):
    area = pi * r**2
    return area

print(str(num_one)+' to the power of '+str(num_two)+' is:', str(num_one**num_two))
#calculating the area of a circle
radius = 30 #radius of a circle
pi = 3.14 #pi value
area_of_circle = pi * radius**2
print('The area of a circle with radius '+str(radius)+' is: '+str(area_of_circle)+' meters square.')
#calculating the circumference of a circle
circum_of_circle = 2 * pi * radius
print('The circumference of a circle with radius '+str(radius)+' is: '+str(circum_of_circle)+' meters.')
#calculating the density of a substance
#mass = 75 #mass in kg
input_radius = input('Enter radius: ')
radius = float(input_radius)    
area_of_circle= calculate_area_of_circle(radius)
print('The area of a circle with radius '+str(radius)+' is: '+str(area_of_circle)+' meters square.')

f_name,l_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Finland', 250, True   
print(f_name, l_name, country, age, is_married)
