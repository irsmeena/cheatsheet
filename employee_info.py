# Define a list of dictionaries to store employee information
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]




# Filters employees whose age is between the given lower and upper limits.
#The result is stored in a list called result and returned.

def get_employees_by_age_range(age_lower_limit, age_upper_limit):
    result = []

    # Loop through each employee in the data #item 
    for item in employee_data:
        # Check if the employee's age is between the given limits
        if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
            result.append(item)  # Add matching employee to the result list #result is the name of the array

    return result  # Return the filtered list

# Function to calculate the average salary of all employees
def calculate_average_salary():
    total = 0     # Variable to store the sum of all salaries
    average = 0   # Will hold the final average

    # Loop through all employees and add up their salaries
    for item in employee_data:
        total += item["salary"]

    # Calculate average salary
    average = total / len(employee_data)

    return round(average, 2)  # Return the average rounded to 2 decimal places

# Function to get employees who belong to a specific department
def get_employees_by_dept(department):
    result = []

    # Loop through each employee
    for item in employee_data:
        # Check if the department matches
        if item["department"] == department:
            result.append(item)

    return result  # Return list of matching employees

# Function to display all employee records in a formatted table
def display_all_records():
    # Print header row with aligned columns
    print(("Name" + "\t" + "Age" + "\t" + "Department" + "\t" + "Salary").expandtabs(15))
    
    # Loop through each employee and print their data
    for item in employee_data:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))

# Function to display only a selected list of employee records (filtered ones)
def display_records(employee_info):
    # Print header row
    print(("Name" + "\t" + "Age" + "\t" + "Department" + "\t" + "Salary").expandtabs(15))
    
    # Loop through the filtered list and print employee info
    for item in employee_info:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))

# Function to show the main menu and process user selections
def display_main_menu():

    # Print menu options
    print("\n----- Employee Information Tracker -----")
    print("Select option\n")
    print("1 - Display all records")
    print("2 - Display average salary")
    print("3 - Display employee within age range")
    print("4 - Display employee in a department")
    print("Q - Quit")

    # Get the user's choice
    option = input("Enter selection => ")

    # Check user's input and call the appropriate function
    if option == '1':
        display_all_records()

    elif option == '2':
        average_salary = calculate_average_salary()
        print("Average salary = " + str(average_salary))

    elif option == '3':
        # Ask for age range limits
        age_lower_limit = input("Age (Lower Limit) = ")
        age_upper_limit = input("Age (Upper Limit) = ")
        # Get matching employees
        employee_info = get_employees_by_age_range(age_lower_limit, age_upper_limit)
        display_records(employee_info)

    elif option == '4':
        # Ask for department name
        department = input("Name of Department = ")
        # Get matching employees
        employee_info = get_employees_by_dept(department)
        display_records(employee_info)

    elif option == 'Q':
        quit()  # Exit the program

# Entry point of the program
def main():
    # Keep showing the menu until user quits
    while True:
        display_main_menu()

# Only run the main function if this script is executed directly
if __name__ == "__main__":
    main()
