# Write a Python Program to Split the array and add the first part to the end
 
arr = list(map(int, input("Enter the array: ").split()))
key = int(input("Enter the key: "))

arr1 = list(arr[:-key])
arr2 = list(arr[-key:])

fianal_arr = arr2 + arr1
print(fianal_arr)