
#Author: Jacob Neaderland
#Lab 11-6
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

#Lab 11-7
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
