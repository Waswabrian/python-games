#Bubble sort algorithm
array = [728,23,4,55,23,545,902,420,674,34,12,70,67,309,82,30,11,234,129]
n = len(array)
print(n)
print(array)

for i in range(n-1):
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            print("sorted array is:",array)