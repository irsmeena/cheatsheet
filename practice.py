employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},

]

employee = employee_data[0]


print(employee_data) #prints the dictionary
print(employee.keys()) #printsdict_keys(['name', 'age', 'department', 'salary'])
print(employee.values())#prints dict_values(['John', 30, 'Sales', 50000])

#prints
#name: John
#age: 30
#department: Sales
#salary: 50000
# Useful for looping through both field names and values.

for key, value in employee.items():
    print(f"{key}: {value}")


#50000
#None (no bonus in dictionary so its assigned none)

print(employee.get("salary"))       
print(employee.get("bonus"))  

#prints {'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000, 'bonus': 1000}
employee.update({"bonus": 1000})
print(employee)

#removes a key and gets its value 
salary = employee.pop("salary")
print(salary)     # Output: 50000
print(employee)   # Now 'salary' is removed


#if the key doesnt exist you can pass it a default value
employee.pop("bonus", 0)