nam = [input("whats your first name? "), input("whats your second name? "), input("whats your third name? "), input("whats your fourth name? "), input("whats your fifth name? ")]
name1 = nam[0]
name2 = nam[1]
name3 = nam[2]
name4 = nam[3]
name5 = nam[4]
def name_multiplication(n1, n2, n3, n4, n5):
    names = [n1, n2, n3, n4, n5]
    prints = 0
    for name in names:
        while prints < len(name):
            print (name)
            prints += 1            
        prints = 0
name_multiplication(name1, name2, name3, name4, name5)
