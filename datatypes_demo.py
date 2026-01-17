intergerVar=int(input("Enter Any Favourite Number:"))
intDecimalvar=float(input("Enter Any Decimal Fauvariote Number:"))
stringVar=input("Enter Your Name:")
booleanVar=bool(False)
bool1var=True
bool2var=bool(input("Enter Only True or Flase:")) # this Line will execute.If You enter Random Stirng it gives True Only.ie
#In Variable bool2var has a Value=True.
'''
Note that by Default Input Function/Method Take input has a String.

'''

print("\nInterger=",intergerVar," Type=",type(intergerVar))
print("\nDecimal=",intDecimalvar," Type=",type(intDecimalvar))
print("\nString=",stringVar," Type=",type(stringVar))
print("\nBoolean=",booleanVar," Type=",type(booleanVar))
print(type(bool1var))
print("Type Of=",type(bool2var)," And Value in Variable is=",bool2var)



'''
Lets Build A Simple Calculator

'''

num1=int(input("Enter Number1:"))
num2=int(input("Enter Number2:"))
print("Addtion of num1=",num1,"=num2=",num2," Answer=",num1+num2)
print("Subtraction of num1=",num1,"=num2=",num2," Answer=",num1-num2)
print("Multiplication of num1=",num1,"=num2=",num2," Answer=",num1*num2)
print("Division of num1=",num1,"=num2=",num2," Answer=",num1/num2)
print("Modulor of num1=",num1,"=num2=",num2," Answer=",num1%num2)
print("Exponent of num1=",num1,"=num2=",num2," Answer=",num1**num2)



'''
Lets Build A More Simple Calculator 
with Error Handling Code
'''

try:
    num1=int(input("Enter Number1:")) #Resusing same name Variable
    num2=int(input("Enter Number2:")) #Resusing same name Variable
    print("Addtion of num1=",num1,"=num2=",num2," Answer=",num1+num2)
    print("Subtraction of num1=",num1,"=num2=",num2," Answer=",num1-num2)
    print("Multiplication of num1=",num1,"=num2=",num2," Answer=",num1*num2)
    print("Division of num1=",num1,"=num2=",num2," Answer=",num1/num2)
    print("Modulor of num1=",num1,"=num2=",num2," Answer=",num1%num2)
    print("Exponent of num1=",num1,"=num2=",num2," Answer=",num1**num2)
    
except ValueError:
    print("OOPs!! Error Occurs You Entered Wrong Data Type")
except ZeroDivisionError:
    print("Oops!! Error Occurs You Cannot divide By Zero")




    













