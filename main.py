import datetime
import time


# function 1 to read the data from the text file
# save the data in a dictionary
def read_file(filename):
    employee_dict = {}

    try:
        # open the file in the read file
        with open(filename, 'r') as file:
            for line in file:
                emp_id, username, join_date, gender, salary = line.strip().split(', ')
                employee_dict[emp_id] = {
                    'username': username,
                    'join_date': join_date,
                    'gender': gender,
                    'salary': int(salary)
                }
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

    return employee_dict


# function 2 to display the data
def display_Data(employee_dict):
    print("Employee Dictionary:")
    print("-" * 20)
    for emp_id, emp_info in employee_dict.items():
        print(f"Employee ID: {emp_id}")
        print(f"Username: {emp_info['username']}")
        print(f"Join Date: {emp_info['join_date']}")
        print(f"Gender: {emp_info['gender']}")
        print(f"Salary: {emp_info['salary']}")
        print("-" * 20)


# function 3  to count the number of female and male employees
def count_gender_employees(employee_dict):
    count_male = 0
    count_female = 0
    for emp_id, emp_info in employee_dict.items():
        if emp_info['gender'] == 'male':
            count_male += 1
        else:
            count_female += 1
    return count_male, count_female


# function 4 to add a new employee to the dictionary
def add_Employee(employee_dict, username, gender, salary):
    emp_id = f"emp{len(employee_dict) + 1:03d}"
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    new_employee = {
        'username': username,
        'join_date': current_date,
        'gender': gender,
        'salary': int(salary)
    }
    employee_dict[emp_id] = new_employee


# function 5 to display the data of the employees registered in the system ordered by date
def display_employees_by_date(employee_dict):
    sorted_employees = sorted(employee_dict.items(), key=lambda x: x[1]['join_date'], reverse=True)
    display_Data(sorted_employees)


# function 6 to change the employee's salary
def change_Employee_Salary(employee_dict, emp_id, new_salary):
    if emp_id in employee_dict:
        employee_dict[emp_id]['salary'] = int(new_salary)
        print("\nSalary updated successfully!\n")
    else:
        print("\nEmployee not found.\n")

    # function 7 to remove a specific employee


def remove_Employee(employee_dict, emp_id):
    if emp_id in employee_dict:
        del employee_dict[emp_id]
        print("\nEmployee removed successfully!\n")
    else:
        print("\nEmployee not found.\n")


# function 8 to increase the employee's salary by a specific percentange
def raise_Employee_Salary(employee_dict, emp_id, percentage):
    if emp_id in employee_dict:
        current_salary = employee_dict[emp_id]['salary']
        increase_amount = int(current_salary * percentage)
        employee_dict[emp_id]['salary'] += increase_amount
        print("\nSalary increased successfully!\n")
    else:
        print("\nEmployee not found.\n")

    # function 9 to save the new data into the original text file


def save_to_file(filename, employee_dict):
    try:
        with open(filename, 'w') as file:
            for emp_id, emp_info in employee_dict.items():
                line = f"{emp_id}, {emp_info['username']}, {emp_info['join_date']}, {emp_info['gender']}, {emp_info['salary']}\n"
                file.write(line)
        print("\nData saved to file successfully!\n")
    except Exception as e:
        print(f"An error occurred while saving the data: {e}")


# function 10 to display the admin menu
def admin_menu():
    print("Admin Menu:")
    print("1. Display Statistics")
    print("2. Add an Employee")
    print("3. Display all Employees")
    print("4. Change Employee's Salary")
    print("5. Remove Employee")
    print("6. Raise Employee's Salary")
    print("7. Exit")


# function 11 to search if the employee's username exists or not
def search_employee_by_username(username, employee_list):
    for employee in employee_list:
        if employee['username'] == username:
            return employee
    return None


# function 12 to customize the greetings based on the employee's gender
def greetings(gender, username):
    if gender == 'male':
        print("Hi Mrs ", username)
    else:
        print("Hi Miss", username)


# function 13 to display the user menu
def user_menu():
    print("User Menu:")
    print("1. Check my Salary")
    print("2. Exit")


# function 14 to check the validity of admin's choice
# choice must be between 1 and 7
def valid_choice(choice, lower_bound, upper_bound):
    while True:
        try:
            if choice >= lower_bound and choice <= upper_bound:
                break
            else:
                choice = int(input("Enter a number between from the above list: "))
        except ValueError:
            print("Invalid input")
    return choice


# function 15 to execute the operation chosen by the admin
def admin_operation(choice):
    if choice == 1:
        print("\nEmployee Gender Count:")
        male_count, female_count = count_gender_employees(employees)
        total_count = len(employees)
        print(f"Male Employees: {male_count} out of {total_count}")
        print(f"Female Employees: {female_count} out of {total_count}")
        print("-" * 20)

    elif choice == 2:
        new_username = input("Enter new employee's username: ")
        new_gender = input("Enter new employee's gender: ")
        new_salary = input("Enter new employee's salary: ")
        add_Employee(employees, new_username, new_gender, new_salary)
        print("\nNew employee added successfully!\n")
        print("-" * 20)

    elif choice == 3:
        display_Data(employees)

    elif choice == 4:
        emp_id_to_change = input("Enter Employee ID whose salary you want to change: ")
        new_salary = input("Enter new salary: ")
        change_Employee_Salary(employees, emp_id_to_change, new_salary)

    elif choice == 5:
        emp_id_to_remove = input("Enter Employee ID to remove: ")
        remove_Employee(employees, emp_id_to_remove)

    elif choice == 6:
        emp_id_to_increase = input("Enter Employee ID to increase salary: ")
        increase_percentage = float(input("Enter increase percentage (e.g., 1.05 for 5% increase): "))
        raise_Employee_Salary(employees, emp_id_to_increase, increase_percentage)

    # function 16 to save the login time of the employee into txt file


# name of txt file will be the id of the employee
def save_login_timestamp(employee_dict):
    employee_id = employee_dict["employee_id"]
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    filename = f"{employee_id}.txt"
    with open(filename, "w") as file:
        file.write(f"Employee ID: {employee_id}\n")
        file.write(f"Login Time: {timestamp}")

    print(f"Login timestamp saved to {filename}")


employee_list = [
    {'employee_id': 'emp001', 'username': 'cdaoud', 'gender': 'male', 'salary': 2500},
    {'employee_id': 'emp002', 'username': 'manuella', 'gender': 'female', 'salary': 1200},
    {'employee_id': 'emp003', 'username': 'sami', 'gender': 'male', 'salary': 500},
    {'employee_id': 'emp004', 'username': 'fatima', 'gender': 'female', 'salary': 800},
    {'employee_id': 'emp005', 'username': 'manal', 'gender': 'female', 'salary': 5125},
    {'employee_id': 'emp006', 'username': 'farah', 'gender': 'female', 'salary': 1000},
    {'employee_id': 'emp007', 'username': 'aly', 'gender': 'male', 'salary': 750},
]

file_name = 'employee_data.txt'
employees = read_file(file_name)
print("*** Welcome to the Employee Database System ****")
print("Login form:")
admin_password = "admin123123"
admin_username = "admin"
count = 5

while (count > 0):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    found_employee = search_employee_by_username(username, employee_list)
    if username == admin_username and password == admin_password:
        while True:
            admin_menu()
            choice = int(input("Enter your choice ( The number should be between 1 and 7 ):"))
            choice = valid_choice(choice, 1, 7)
            print("the new choice:", choice)
            admin_operation(choice)
            print("-" * 20)
            if choice == 7:
                save_to_file(file_name, employees)
                print("Exiting the program.")
                break
        break
    elif found_employee:
        print("Employee found:")
        greetings(found_employee['gender'], found_employee['username'])
        while True:
            user_menu()
            choice = int(input("Enter your choice ( The number should be between 1 and 2 ):"))
            choice = valid_choice(choice, 1, 2)
            print("the new choice:", choice)
            print("-" * 20)
            if choice == 1:
                print("Your salary is", found_employee['salary'])
                print("-" * 20)
            elif choice == 2:
                # save login time of the employee into txt tile named with the id of the employer
                login_time = time.strftime("%Y-%m-%d %H:%M:%S")
                save_login_timestamp(found_employee)
                print("Exiting the program.")
                print("-" * 20)
                # Save timestamp to a file (not implemented here)
                break
        break
    else:
        count = count - 1
        print(f"Incorrect Username and/or Password. {count} attempts remaining.")

    if count == 0:
        print("Max attempts reached. Exiting...")