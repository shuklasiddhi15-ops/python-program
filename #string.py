#string
Vowels = "AEIOUaeiou"
Word = input("enter your string")
count=0
for i in Word :
    if i in Vowels:
        count += 1
print(count)
# second type in vowel
Vowels = "AEIOUaeiou"
Word = input("enter your string")
for i in Word:
    if i in Vowels :
        print ("yes")
else:
    print("no")
#next prg
Number =input("enter your string")
print (Number[:: -1])
type(Number)