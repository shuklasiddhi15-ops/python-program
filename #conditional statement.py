#conditional statement
Age = int(input("enter your age:"))
Nationality = input("enter your nationality:")
if Age>= 18 and Nationality == "Indian":
   print("yes")
else:
  print("no")

  #grading system
Marks = int(input("enter your marks:"))
if Marks>= 90:
   print("A")
elif Marks>=75:
   print("B")
else:
   print("fail")

#hw question
#even or odd prg
num = int(input("enter a number:"))
if num % 2 == 0:
   print("Even")
else:
   print("odd")
#largest of two number
num1=int(input("enter a number:"))
num2= int(input("enter a number"))
if num1>num2:
  print("num1 ")
else:
    print("num2")
