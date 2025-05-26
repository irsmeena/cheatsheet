import employee_info as empInfo



def test_get_employees_by_age_range():
    # Test case 1: Employees in the age range of 25 to 35
    exp_result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    result = empInfo.get_employees_by_age_range(25, 35) 
    assert(result==exp_result)  # Assuming the expected result is correct, adjust as per your data


def test_calculate_average_salary():
    # Test case 2: Average salary of all employees
    result = empInfo.calculate_average_salary()
    assert(result == 60166.67)  # Assuming the average salary is 50000, adjust as per your data

def test_get_employees_by_dept():
    # Test case 3: Employees in the 'Sales' department
    exp_result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    result = empInfo.get_employees_by_dept('Sales') 

    assert(result==exp_result)  # Assuming the expected result is correct, adjust as per your data  
    