while 1>0:
    temp = input("Pls enter the number: ")
    num = int(temp)

    def check(i):
        if i == 0:
            print("Number is Odd")
        elif i % 2 == 0:
            print("Number is Even")
        else:
            print("Number is Odd")
    
    check(num)
