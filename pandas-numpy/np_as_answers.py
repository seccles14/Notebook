'''
refer to numpy_assignment.md for questions
'''

import numpy as np


#1
def array_norm(input):
    norm = (input - input.mean())/np.std(input)
    return norm


x = np.array([[1,2,3,4]])
print(array_norm(x))



#2
def array_2(input):
    norm = (input - input.mean(axis = 1))/input.std(axis=1)
    return norm

#create a 3x3 matrix with range to 9
y = np.arange(9).reshape(3,3)
print(array_2(y))

#3
def array(num_cols, num_rows,fill_value):
    new = np.zeros((num_rows, num_cols))+fill_value
    return new

print(array(num_cols=4, num_rows = 3, fill_value=2))

#4

## answer is close but not right
#def math(input, x, op):
    # this is defining the operators that is inputted to key the commands
    #op_def = {'+': 1, '-': np.subtract, '*': np.multiply, '/': np.divide}
    #ar = op_def[op](input,x)
    #return ar

#print(math(input=[[1,2,3,4]], x= 2, op = '+'))


def math(input, x, op):
    if op == "+":
        ar = np.add(input,x)
    elif op == "-":
        ar = np.subtract(input,x)
    elif op == "*":
        ar = np.multiply(input,x)
    else:
        ar = np.divide(input,x)
    return ar

print(math(input = [[1,2,3,4]], x=2, op="+"))

#5
def arr(x):
    ##random.rand gives numbers 0 to 1
    array = np.random.rand(1,x)
    return array
print(arr(5))

#6
def random_matrix(num_rows, num_cols):
    array = np.random.rand(num_rows, num_cols)
    return array
print(random_matrix(2,4))

#7
def random(input, x):
    rand = np.random.choice(input, x)
    return rand
t = np.arange(9)
print(random(t,2))


#8
def replace_max(input):
#replace the max element in the array with 0.

    input[input.argmax()] = 0
    return input

t = np.arange(9)
print(replace_max(t))

#9
def cum_sum(x):
#cumulative sum of x number of values in a 1-D array cum sum of 0 to x
    array = np.arange(x+1)
    csum = array.cumsum()
    # cumsum is creating an array adding up, and we only want last one
    return csum[-1]
print(cum_sum(4))

#10
def dot_prod(mat1, mat2):
#dot product between two 2D arrays

    return np.dot(mat1,mat2)

v = np.arange(9).reshape(3,3)
print(dot_prod(v,v))

#11
def element_mult(mat1, mat2):
#element-wise multiplication between two 2-D arrays
    return mat1 * mat2

v = np.arange(9).reshape(3,3)
print(element_mult(v,v))


#12
def top_five(array):
#return the top 5 elements of the inputted 1D array
    array.sort()
    return array[-5:]

t = np.arange(9)
print(top_five(t))


#13
def small_five(array):
#return the smallest 5 elements of each column of a 2D array
    array.sort(axis = 0)
    return array[0:5]

v = np.arange(81).reshape(9,9)
print(small_five(v))


#Extra Credit
def cum_sum_n(x):
#return the cumulutive sum of the column means of a matrix that is max size n x n with x num_elements
# 1. create an array 0 to input, x
# 2. reshape it to largest n * n array, discarding extra num_element
# 3. returns the cum sum of the column means

    arr = np.arange(x) #1
    shape = int(x ** 0.5) #2 gives you max size matrix (shape x shape) with number of values, x

    array_shape = arr[:shape **2].reshape(shape,shape) #creates matrix, from 0 to shape**2, with size shape x shape
    csum = array_shape.mean(axis = 0).cumsum(axis = 0) #3 cumsum of the means of each column in matrix "array_shape"

    return csum[-1] #use -1 to only refer to the last value of the cum sum (single value)

x = 5
print(cum_sum_n(x))
