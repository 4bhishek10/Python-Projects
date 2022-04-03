def differenceofSum(n, m):
    diff =0
    sumDiv = 0
    sumNotDiv = 0
    for i in range(1, m+1):
        if i % n != 0:
            sumNotDiv += i
        elif i % n == 0:
            sumDiv += i
    diff = sumNotDiv - sumDiv
    
    return diff

n = int(input("pls enter n: "))
m = int(input("pls enter m: "))

print(differenceofSum(n, m))
