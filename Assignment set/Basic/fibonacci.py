stri = input("how many no you want: ")
num = int(stri)
fib = []
sum = 0

if num == 1 :
    fib.append(0)
elif num == 2:
    fib.append(0)
    fib.append(1)

else :
    fib.append(0)
    fib.append(1)
    for i in range(0,num-2):
        
        sum = fib[i+1]+fib[i]
        fib.append(sum)
        #sum = 0

print(fib)