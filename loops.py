#print no
i = int(input("enter your number"))
for i in range (1,21):
    print (i)
#WHILE LOOP
i = 1
while i <= 20 :
 print (i)
 i+= 1

#print even number
#for loop
for i in range (1,51):
   if i % 2 == 0:
    print (f"{i} is Even")
   else:
     print (f"{i} is Odd")
#while loop
i = 1
while i <= 50 :
  if i % 2 == 0 :
    print(f"{i} is even")
  else:
    print(f"{i} is odd")
  i +=1
#multiplication table
num = int(input("enter your table"))
for i in range (1,11):
  print(f"{num}*{i} ={num*i}")
# while
num = int(input("enter your table"))
i = 1
while i<11:
  print(f"{num}*{i}={num*i}")
  i +=1 
# sum of first n number
num = int (input("enter your number:"))
sum = 0
for i in range (1,num+1):
  sum += i
  print (sum)

#while
num =int(input("enter you number :"))
sum = 0
i =1
while i<= num:
  sum += i
  i+=1
print(sum)
#FACTORIAL
num = int(input("enter your number :"))
fact = 0
for i in range (1,num+1):
  fact *= 1
  print(fact)