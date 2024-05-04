app = [
    [1, "Hany", 3.8],
    [2, "Mostafa", 3.5],
    [3, "Sara", 3.2],
    [4, "Yassin", 3.9],
    [5, "Zeyad", 1.6],
    [5, "Mohamed", 2.6]
]
accepted=[]
rejected=[]
waitlisted=[]

def add():
    app_id = len(app) +1
    name = input("Please Enter Applicant's Name ")
    gpa = float(input("Please Enter Applicant's GPA "))
    app.append([app_id, name, gpa])
    print("Success")
    print("Current Applicants")
    print(app)

def analyze():

  for applicant in app:
    id = applicant[0]
    name = applicant[1]
    gpa = applicant[2]


    if gpa > 3.5:
      accepted.append([id, name, gpa])  
    elif gpa >= 3:  
      waitlisted.append([id, name, gpa])  
    else:
      rejected.append([id, name, gpa]) 




while True:
        print("Please Enter You Chocie")
        print("1. Add Applicant")
        print("2. Analyze Applicant Data")
        print("3. Generate Admissions Decision")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add()
        elif choice == "2":
            analyze()
            print("Please Run Choice 3 To Review Results")
        elif choice == "3":
            print("Please Run Choice 2 To Generate Results")
            print("Acepted" + ": "+str(len(accepted)))
            print(accepted)
            print('=' * 50)
            print("Waitlisted" + ": "+ str(len(waitlisted)))
            print(waitlisted)
            print('=' * 50)            
            print("Rejcted" + ": "+ str(len(rejected)))
            print(rejected)
            print('=' * 50)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")