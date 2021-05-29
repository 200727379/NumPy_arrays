import numpy as np  # to start using Numpy and all of the functions available in Numpy, you'll need to import items
print("---------------Array 1-------------------------------\n")
my_arr1 = np.array([40, 72, 96, 100]) #create one dimensional array called my_arr1 using regular Python list
print(my_arr1)  #print my_arr1


print("\n\n--------------Array 2--------------------------------\n")
my_arr2 = np.array([(42, 55, 83, 77), (100, 12, 28, 46)])# creating two dimensional array called my_arr2
print(my_arr2)


print("\n\n------------------Array 3----------------------------\n")
my_arr3 = np.zeros((3, 4))  #creating 3 rows, 4 columns array full of zeros. Note the use of function "zero()"
print(my_arr3)


print("\n\n----------------Array 4------------------------------\n")
my_arr4 = np.ones((5, 6))  #creating 5 rows, 6 columns array full of ones. Note the use of function "one()"
print(my_arr4)


print("\n\n----------------Array 5------------------------------\n")
my_arr5 = np.zeros((3, 4), dtype = np.int16)  #dtype specified
print(my_arr5)


print("\n\n----------------Array 6------------------------------\n")
my_arr6 = np.ones((5, 6), dtype = np.int16)  #dtype specified
print(my_arr6)


print("\n\n----------------Array 7------------------------------\n")
my_arr7 = np.empty((2,3)) # the function "empty" create array whose initial content is random.
print(my_arr7)


print("\n\n----------------Array 8------------------------------\n")
my_arr8 =np.arange(10, 100, 5)  #range of numbers between 10 and 100 with a step of 5 between the numbers
print(my_arr8)


print("\n\n----------------Array 9------------------------------\n")
my_arr9 = np.linspace(0, 200, 9)  #9 numbers from 0 to 200. Note function "linspace()"
print(my_arr9)
