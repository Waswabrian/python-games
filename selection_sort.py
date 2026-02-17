#selection sort algorithm practice(12/9/2025)
array = [344,874,13,546,43213,246,746,32,11,90,450,420,345,23,567,34,254,6,667,453,90]
n=len(array)

for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if array[j] < array[min_index]:
            min_index = j
        
    # new_value = array.pop(min_index)
    # array.insert(i, new_value) 
    array[min_index], array[i] = array[i], array[min_index]
    print(array)
