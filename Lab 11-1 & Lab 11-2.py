num_a = int(input("What is your first number? "))
num_b = int(input("What is your second number? "))
def find_evens(a, b):
    numl = [a, b]
    numl.sort()
    even = []
    for num in range(numl[0], numl[1]):
        if num % 2 == 0:
            even.append(num)
    print (even)
find_evens(num_a, num_b)


word = input("What is your word? ")
def is_palindrome(pal):
    pal = pal.lower()
    pal = str(pal)
    bac = []
    itteration = 0
    pal = " ".join(pal)
    pal = pal.replace(" ", "")
    leng = len(pal)
    print(pal)
    for back in range(leng):
        bac.append(pal[leng-1])
        leng -= 1
        itteration += 1
    bac = " ".join(bac)
    bac = bac.replace(" ", "")
    print (bac)
    if bac == pal:
        print ("True")
    else:
        print ("False")
is_palindrome (word)
