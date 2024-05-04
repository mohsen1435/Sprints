
#Variables Promt
num1 = input("Please Enter The First Number ")
num2 = input("Please Enter The Second Number ")

#Calculation
sum_result = int(num1) + int(num2)
diff_result = int(num1) - int(num2)
mul_result = float(num1) * float(num2)
div_result = float(num1) / float(num2)
print(f"You Number Are: {num1} ,{num2}")
print(f"Sum={sum_result} , Diff={diff_result} ,Mul={mul_result} ,Div={div_result}")

#Comparison
if num1>num2:
    print("Num1 Is Bigger Than Num2")
elif num2>num1:
    print("Num2 Is Bigger Than Num1")  
else:
    print("Num1 Equals Num2") 

#Even And Odd
if sum_result % 2 == 0:
    print("Sum Is Even")
else:
     print("Sum Is Odd")  

#Comparison 
if num1>num2:
    print("Num1 Is Bigger Than Num2")
elif num2>num1:
    print("Num2 Is Bigger Than Num1")  
else:
    print("Num1 Equals Num2") 
     
