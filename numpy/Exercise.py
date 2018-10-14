import numpy as np

#1. Create arrays of 10 zeros
arr_zero = np.zeros((10))
print(arr_zero)

#2. Create arrays of 10 ones
arr_ones = np.ones(10)
print(arr_ones)

# 3. Create array 10 fives
a = np.empty(10)
a.fill(5)
print(a)

#4.Create array of integers fro 10  to 50
arr = np.arange(10,51)
print(arr)

#5.Create array of all even Integers between 10 to 50

arr_even = np.arange(10,51,2)
print(arr_even)

arr_even = np.arange(10,51)
arr_even = arr_even[arr_even%2==0]
print(arr_even)

# 6.Create 3 x 3 matrix from 0 to 8
matrix_3x3 = np.arange(0,9).reshape(3,3)
print(matrix_3x3)

#7.Create 3 x 3 identical matrix
identical_3x3 = np.eye(3)
print(identical_3x3)


#8.Use numpy to generate a random number between 0 and 1
rabd_float = np.random.uniform(0,1,10)
print(rabd_float)

#9.Create an array of uniform distributed random numbers
var9 = np.random.randn(25)
print(var9)

#10.Create 2D matrix between 0 and 1 with 100 elements

var5 = np.linspace(0,1,100).reshape(10,10)
print(var5)
