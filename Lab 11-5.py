name1 = input("whats your first name")
name2 = input("whats your second name")
name3 = input("whats your third name")
name4 = input("whats your fourth name")
name5 = input("whats your fifth name")
print(name1.unique())
def name_multiplication(n1, n2, n3, n4, n5):
    names = [n1, n2, n3, n4, n5]
    prints = 0
    for name in names:
        while prints < len(name):
            print (name)
            prints += 1            
        prints = 0
name_multiplication(name1, name2, name3, name4, name5)
