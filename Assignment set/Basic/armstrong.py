tmp = int(input("Pls enter the number: "))
sum = 0
order = len(str(tmp))
num = tmp

while (num>0):
    digit = num % 10
    sum += digit ** order
    num = num // 10
if(sum == tmp):
    print("Armstrong Number")
else:
    print("Not An Armstron Number")
    