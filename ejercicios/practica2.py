'''
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''

## solución con recursividad

def grow(arr):
    result = 1
    def recursividad(arr, result):
        if len(arr) == 0:
            return result
        
        result *= arr[0]
            
        return recursividad(arr[1:], result)
    return recursividad(arr, result)

## solución con reduce

from functools import reduce
def grow(arr):
    def mult(a, b):
        return a*b
    return reduce(mult, arr)