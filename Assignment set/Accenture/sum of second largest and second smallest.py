length = int(input())
arr = list(map(int, input().split()))
even_arr = []
odd_arr = []
for i in range(length):
    if i % 2 == 0:
        even_arr.append(arr[i])
    else:
        odd_arr.append(arr[i])
even_arr.sort()
odd_arr.sort()
sum = even_arr[len(even_arr)-2] + odd_arr[len(odd_arr)-2]
print(sum)