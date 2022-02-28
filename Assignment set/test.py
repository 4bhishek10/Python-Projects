
def alternateMerge(arr1, arr2, n1, n2, arr3) :
	i = 0; j = 0; k = 0


	while (i < n1 and j < n2) :
		arr3[k] = arr1[i]
		i += 1
		k += 1
		
		arr3[k] = arr2[j]
		j += 1
		k += 1
	


	while (i < n1) :
		arr3[k] = arr1[i]
		i += 1
		k += 1

	while (j < n2) :
		arr3[k] = arr2[j]
		k += 1
		j += 1
		

arr1 = [1, 3, 5, 7, 9, 11]
n1 = len(arr1)

arr2 = [2, 4, 6, 8]
n2 = len(arr2)

arr3= [0] *(n1 + n2)
alternateMerge(arr1, arr2, n1, n2, arr3)

print("Array after merging")
for i in range(0, (n1 + n2)) :
	print(arr3[i] , end = " ")