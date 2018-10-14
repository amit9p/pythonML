import numpy as np

arr = np.random.randint(10,20,15)
print(arr)
#To find number stored at index position 8
print(str(arr[8]))

#To find the number stored from index 0 to 5
print(str(arr[0:5]))

#Broadcasting set of values , say I want to change all values from index 0 to 5 to 100
arr[0:5] = 100
print(arr)

#Slicing of array
slice_of_arr = arr[0:6]
print(slice_of_arr)

#Broadcast  all the vales to slices
slice_of_arr[:] = 99
print(slice_of_arr)

#Call arr and check for the values, orignal array also would be changed
print(arr)

#To copy an array
arr_cpy = arr.copy()
print(arr_cpy)

#Broadcast 100 to arr_cpy
arr_cpy [:] = 100
print(arr_cpy)

#Check original array arr, its unaffected
print(arr)

#Create 2D array
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
print(arr_2d[0][0])
print(arr_2d[0,0])
print(arr_2d[:2,2:])
print(arr_2d[:3])

#Create array from 1 to 10 and create a boolean array based on condition > 5. create a new array of true values
arr = np.arange(1,11)
bool_arr = arr >5
print(bool_arr)
arrbool = arr[bool_arr]
print(arrbool)

#Selecting elements from 2D  matrix
arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)
print(arr_2d[1:3,3:5])
