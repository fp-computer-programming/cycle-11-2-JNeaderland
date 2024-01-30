"""

Create a Python file named lab_10-1.py
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Using a while loop, write a program that prompts the user to input a number.
If the user inputs a number, add that to the sum of the previous numbers entered.
If the user enters -1, the program should end and display the sum of all the numbers entered.
Be sure the program uses a break statement
_____________________________________________________________________________________________________________

Create a Python file named lab_10-2.py
Using the same approach as lab 1, write a program that prints all the numbers that are multiples of 3 in a list. Be sure your program uses a continue statemen


"""

#Author: Jacob Neaderland
#Lab 10-1
num = input("What is your number? ")
numi = int(num)
intn = int(0)
print (numi)
nsum = 0
while type(numi) == type(intn): #Always active
    nsum = nsum + numi # Adds current number to the sum
    num = input("What is your number? ")
    numi = int(num)
    if numi == -1:
        break
print ("Sum equals ", nsum)

#Lab 10-2
num = "0"
numi = int(0)
intn = int(0)
print (numi)
nsum = 0
tlist = [] #To store the values divisible by 3
while type(numi) == type(intn): #Always active
    num = input("What is your number? ")
    numi = int(num)
    if numi == -1:
        break
    if numi % 3 != 0: #Skips numbers that aren't divisible by 3
        continue
    tlist.append(numi) #Adds the ones that are to the list
print (tlist)
