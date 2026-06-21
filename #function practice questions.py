# function practice question
def number_sum(Num):
    sum = 0
    for i in range (1, Num + 1):
        sum += i
        print(sum)

number_sum(11)
# print sum of two number
def sum_num(a,b):
    Sum = a+b
    print(Sum)
sum_num ( 2,3)
#subration of two number
def  sub_num(a,b):
    Sub= a-b
    print(Sub)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sub_num(a, b)
#multifly of two number
def multiply_num (a,b):
    Multiply= a*b
    print(Multiply)
a= int(input("enter your number"))
b= int (input("enter your number"))
multiply_num(a,b)

#division of two number
def division_num (a,b):
    Division= a/b
    print(Division)
a= int(input("enter your number"))
b= int (input("enter your number"))
division_num(a,b)

#moduslus of  two number
def modulus_num(a,b):
    Modulus=a%b
    print(Modulus)
modulus_num(2,4)

#hello world
def greet(Name):
    print(f"hello {Name}")
greet ("siddhi")

#comparision
def compar_num(a,b):
    Compar = a==b
    print(Compar)
compar_num(2,6)

 #variable name by function
def student_name():
    print(Name)
Name = input("enter your name")
student_name ()

def marks_num(marks):
  print(Marks)
  print (type(Marks))
Marks = input("Enter your marks: ")
marks_num("marks")
def age_num(Age):
     name = "vikas"
     age ="22"  
     age1 = int(age)
     print(age1)
age_num("Age")

#conditionalstatement by function
#grading system
def grading_system():
    if Marks>= 90:
        print("A")
    elif Marks>= 75:
        print("B")
    else:
        print("Fail")
Marks= int(input("enter your marks:"))
grading_system()
# even odd function
def Even_Odd (Num):
   num = int(input("enter your number"))
   if num % 2 == 0:
       print (f"{num}is even")
   else:
       print(f"{num} is odd")
Even_Odd ("Num")
# voting criterion function
def voting_criteria(Age,Nationality):
    if Age>=18 and Nationality == "Indian":
        print("yes")
    else:
        print("no")
Age = int(input("enter your age"))
Nationality = input("enter your nationality")
voting_criteria(21,"Indian")
#largest of two number
def large_num(Num):
    num1 = int(input("enter your num"))
    num2 = int(input("enter your num"))
    if num1>num2:
        print(num1)
    else:
        print(num2)
large_num("Num")
#positive negative zero
def positive_negative_zero(Num):
    num = int(input("enter your number"))
    if num>0:
        print("positive")
    elif num<0:
        print("negative")
    else:
        print("zero")
positive_negative_zero("Num")

#loops question in function
#Print no
def Print_num(Num):
    i = int(input("enter your num"))
    for i in range (1,11):
        print(i)
Print_num("Num")
#while
def Print_num(Num):
     i = int(input("enter your num"))
     i = 1
     while i<=10:
         print(i)
         i += 1
Print_num("Num")

#print even number function
#for
def Even_Odd (Num):
    for i in range (1,51):
        if i % 2 == 0:
            print (f"{i} is even")
        else:
            print(f"{i} is odd")
Even_Odd("Num")

#while
def Even_Odd(Num):
    i = 1
    while i <= 50:
        if i % 2==0:
         print(f"{i} is even")
        else:
         print(f"{i} is odd")
        i+=1
Even_Odd("Num")
#multiplication table  by function
def Multiply_num(Num):
    num = int(input("enter your table"))
    for i in range (1,11):
        print(f"{i}*{num}={num*i}")
Multiply_num("Num")
#while
def Multiply_num (Num):
    num= int(input("enter your table"))
    i = 1
    while i <11:
        print (f"{i}*{num} ={i*num}")
        i += 1
Multiply_num("Num")
# sum of first n num
def first_num(Num):
    num = int(input("enter your num"))
    sum = 0
    for i in range(1,num + 1):
        sum += i
        print(sum)
first_num("Num")
#while
def first_num(Num):
    num = int(input("enter your num"))
    sum=0
    i =1
    while i <= num:
        sum += i
        i+=1
        print(sum)
first_num("Num")
#factorial
def fact_num(Num):
    num = int(input("enter your number"))
    fact = 1
    for i in range (1,num+1):
        fact *= i
        print(fact)
fact_num("Num") 
#while
def fact_num(Num):
    num = int (input("enter your number"))
    fact = 1
    i = 1
    while i<= num:
        fact*=i
        i += 1
        print(fact)
fact_num("Num")
def factorial(num):
    if num==0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(5))

# recursion
def show(n):
    if n== 0:
        return
    print(n)
    show(n-1)
show(5)
def show (n):
    if n>10:
        return
    print(n)
    show(n+1)
show(5)




        






