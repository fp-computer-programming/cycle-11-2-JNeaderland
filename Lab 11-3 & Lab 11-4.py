from random import seed
from random import randint
seed(0)
rand = randint(0,100)
def randnum(num):
    guess = input("What is your guess? ")
    while guess != num:
        print ("Pease try again")
        guess = input("What is your guess? ")
randnum(67)

def fibonacci (numnum):
    nums = 0
    sequence = [0, 1]
    leng = 2
    while nums != numnum:
        leng = len(sequence)
        sequence.append(sequence[leng-1] + sequence[leng-2])
        nums += 1
    print (sequence)
fibonacci(int(input("How long would you like it to be? ")))