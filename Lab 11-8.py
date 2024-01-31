def length_multiples (lst):
    lst = list(lst)
    newl = []
    for a, b in enumerate(lst):
        newl.append(b * a)
    print (newl)
testl = [0, 1, 2, 3, 4, 5]    
length_multiples (testl)
testl = [0, 1.5, 2, 3.5, 4, 5.5]    
length_multiples (testl)
testl = ["a", "b", "c", "d", "e"]    
length_multiples (testl)