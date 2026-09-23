#Jeffrey Almendarez
#CMP131
#Week4
#Lab02
#Arithmetic_operations
#9/23/26

num1=float(input("Enter the first number:")) #We are prompting the user for two numbers and it will convert it as a whole number or decimal.
num2=float(input("Enter the second number:"))
addition=num1+num2 #Both of variables displaying the addition
subtraction=num1-num2 #The variables will display the subtraction
multiplication=num1*num2 #Will show the multiplcation between them
division=num1/num2 #The division between the two varibables
power=num1**num2 #Will show us the variables exponent 
average=(num1+num2)/2 #Display the average for us between the two variables
print(f" First Number : {num1}") #Ask for the user to input the first number
print(f" Second Number : {num2}") #Ask for the user to input the second number.
print(f" Addition (+):{num1} + {num2} = {addition:,.2f}") #Takes our value down afterwards and adds both of them
print(f" Subtraction (-): {num1} - {num2} = {subtraction:,.2f}")#Subtracting the values we input displaying our output
print(f" Multiplication(*): {num1}*{num2}={multiplication:,.2f}") #Multiplying our values with the asterik**
print(f"Division (/): {num1}/{num2}={division:,.2f}")
print(f"Power (^): {num1}**{num2}={power:,.2f}") #Calculates the variables and then adds together
print(f" Average: ({num1} +{num2})/2 = {average:,.2f}") #It calculates what is in our parenthesis first then calculates the divsion to find our average.