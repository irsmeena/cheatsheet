
#singular list of ditionary
price_list = {
    'apple': 1.20,
    'orange': 1.40,
    'watermelon': 6.50
}


print(price_list['apple'])     # Output: 1.20
print(price_list.get('orange'))  # Output: 1.40


price_list['apple'] = 1.50 # modify value 

price_list['banana'] = 0.99 # add a new item 



#list of dictionaries
employee_data = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25}
]


#access specific dictionary by index 
print(employee_data[0])       # Output: {'name': 'John', 'age': 30}
print(employee_data[1])       # Output: {'name': 'Jane', 'age': 25}


#access specific value inside the dictionary 
print(employee_data[0]['name'])   # Output: John
print(employee_data[1]['age'])    # Output: 25


#loop through the list 
for employee in employee_data:
    print(employee['name'])  # Prints all employee names

