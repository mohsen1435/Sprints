emp=[
    [1, "Hany","IT" ,3800],
    [2, "Mostafa","IT" ,3050],
    [3, "Sara","IT" ,3882],
    [4, "Yassin","IT" ,3779],
    [5, "Zeyad","IT" ,1446],
    [5, "Mohamed", "IT",2446]
]

def add(name,dep,salary):
    id = len(emp) +1
    try:
     salary = int(salary)
    except:
     print("Error: Invalid salary entered. Please enter a number.")
     return  
    emp.append([id, name, dep, salary])

def update_employee(uid, change, value):
    for employee in emp:
        if employee[0] == uid:
            if change == 'name':
                employee[1] = value
            elif change == 'department':
                employee[2] = value
            elif change == 'salary':
                try:
                    employee[3] = int(value)
                except:
                    print("Invalid salary")
                    return
            print("updated successfully.")
            return
    print("ID not found.")  

    
def gen():
    if len(emp) == 0 :
        print("No employees to generate a report.")
        return
    
    print("Employee Report:")
    print("ID Name Department Salary ")
    for employee in emp:
        print(f"ID = {employee[0]}")
        print(f"Name = {employee[1]}")
        print(f"Department = {employee[2]}")
        print(f"Salary = {employee[3]}")
        print('=' * 10)




while True:
        print("Please Enter You Chocie")
        print("1. Add Employee")
        print("2. Update Employee Information") 
        print("3. Generate Employee Report")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
             name = input("Please enter employee name: ")
             dep =  input("Please enter department name: ")
             salary = input("Please enter salary: ")
             add(name,dep,salary)
        elif choice == "2":
            uid = int(input("Enter the ID of the employee you want to update: "))
            change = input("Enter the field to update (name, department, or salary): ")
            value = input("Enter the new value: ")
            update_employee(uid, change, value)
        elif choice == "3":
            gen()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")