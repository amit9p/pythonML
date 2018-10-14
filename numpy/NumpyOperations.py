import numpy as np

#Array with Array
#Array with Scalar
#Universal Array Function

arr = np.arange(0,11)
print(arr)

#Addition of 2 array elements

add_arr = arr + arr
print(add_arr)

#Add 100 to each element of array
arr_100 = arr + 100
print(arr_100)

#Universal Array Functions
#If you wantto take square root of each element then
arr_sqrt = np.sqrt(arr_100)
print(arr_sqrt)

#Find min max out of array
arr_min = np.min(arr_100)
print(arr_min)
