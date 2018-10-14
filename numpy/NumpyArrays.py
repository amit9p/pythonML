import numpy as np

my_list = [1,2,3]

arr = np.array(my_list)
print(arr)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
two_d_arr = np.array(my_mat)
print(two_d_arr)


#Create an array of 0 to 10
var1 = np.arange(0,10)
print(var1)

#Create an array of even numbers between 0 and 11
var2 = np.arange(0,11,2)
print(var2)

#Create multi dimension array of zeros
var3 = np.zeros((5,2))
print(var3)

var4 = np.ones((5,2))
print(var4)

#Create an array of 10 numbers between 0-5 ,
var5 = np.linspace(0,5,10)
print(var5)

#Create two diminsion identity matrix
var6 = np.eye(2)
print(var6)

#Create array with random function sing dimension
var7 = np.random.rand(10)
print(var7)

#Create array with random function 2 dimension
var8 = np.random.rand(10,5)
print(var8)

#create array not from uniform distribution
var9 = np.random.randn(2)
print(var9)

#Create array of random integer randint(low,high, actualsize)
var10 = np.random.randint(5,10,10)
print(var10)

#reshape numpy array, you can convert 0to24 one dimension array to 2 dimension array
arr = np.arange(25)
var11 = arr.reshape(5,5)
print(var11)

# To find the min and max of the numpy array
arr1 = np.arange(20)
min = arr1.min()
max = arr1.max()
print('min :'+ str(min)+"--"+"max :"+ str(max))

#To find the min and max position in the numpy array
print("Max position :"+ str(arr1.argmax()))
print("Min position :"+ str(arr1.argmin()))

#To get the data type of array
print(str(arr.dtype))
