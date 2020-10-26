import numpy as np
import sys

'''
The implementation of counting number of inversion using
Merge Sort algorithm. 
This example is a special case where the numbers are supposed 
to be equal to their position. In this case, a simple method 
of adding the absolute value of difference between value 
and position of number can be applied to count the numebr 
of inversion
'''

def count_inversion(a):

    def merge_split_inversion(left,right):
        l = len(left) + len(right)
        sorted_a = []
        i = 0
        j = 0
        inversion = 0
        for k in range(l):
            # Append all the remaining of an array if
            # another one goes into end
            if i == len(left):
                sorted_a += right[j:]
                break
            elif j == len(right):
                sorted_a += left[i:]
                break
            elif left[i] < right[j]:
                sorted_a.append(left[i])
                i += 1
            else:
                sorted_a.append(right[j])
                j += 1
                inversion += len(left) - i
        return sorted_a, inversion


    if len(a) == 1:
        return a,0
    else:
        sorted_left, left_inversion = count_inversion(a[:len(a)//2])
        sorted_right, right_inversion = count_inversion(a[len(a)//2:])
        sorted_a, split_inversion = merge_split_inversion(sorted_left, sorted_right)

        return sorted_a, left_inversion + right_inversion + split_inversion

filename = sys.argv[1]
input_array = []

lines = open(filename,'r').readlines()
for num in lines:
    input_array.append(int(num.strip('\n')))


sorted_array, inversion = count_inversion(input_array)

if sorted(sorted_array) == sorted_array:
    print('Correct!')
    print(inversion)
