'''
Write a Python that prints the sum of
two floating point numbers, the difference
between two integers, and the product of 
a floating point number and an integer. 
In each case, have the program print out 
the data type of the resulting answer.

'''
def float_sum(a,b):
    sum = float(a + b)
    print(f"Sum = {sum} Data type = {type(sum)}")
    
def int_diff(x,y):
    diff = int(x - y)
    print(f"Difference = {diff} Data type = {type(diff)}")
    
def prod_float_int(n,m):
    prod = n * m
    print(f"Product = {prod} Data type = {type(sum)}")
    
float_sum(1.1, 2.2)
int_diff(50, 43)
prod_float_int(6.7, 3) 