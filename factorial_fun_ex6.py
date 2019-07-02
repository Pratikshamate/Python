def factorial(a):
    if a <=0:
        print("enter positive integer")
    else:
        for i in range(1,a):
            a = a * i
    
        print(a)


factorial(6)