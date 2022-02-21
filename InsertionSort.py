list1 = [5,6,87,8,65,4,3,2,4,5,6,7,9,9,4]

def fnInsertionSort(list1):
	
	for i in range(1, len(list1)):		
		
		while i > 0 and list1[i] < list1[i-1]:
			list1[i], list1[i-1] = list1[i-1], list1[i]
			i -= 1
			
	return (list1)
	
print (fnInsertionSort(list1))
