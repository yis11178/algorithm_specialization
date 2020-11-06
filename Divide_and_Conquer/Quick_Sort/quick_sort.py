import sys
import argparse
from statistics import median

def partition(array, pivot_pos):
    # returns the partitioned array and the position of pivot.
    array[0], array[pivot_pos] = array[pivot_pos], array[0]
    j = 0
    for i in range(1, len(array)):
        if array[i] < array[0]:
            array[j+1], array[i] = array[i], array[j+1]
            j += 1
    
    array[0], array[j] = array[j], array[0]

    return array, j


def quick_sort(args, array):
    # length of the array
    l = len(array)
    if l == 0:
        return [], 0
    elif l == 1:
        return array, 0
    else:
        if args.pivot == 'first':
            pivot_pos = 0
        elif args.pivot == 'last':
            pivot_pos = -1
        else:
            # position of middle number of the array
            middle_pos = l//2 - ((l+1)%2)
            three = [array[0], array[middle_pos], array[-1]]
            m = median(three)
            pos = three.index(m)
            # median among first, middle and last element of the array
            if pos == 1:
                pivot_pos = middle_pos
            elif pos==2:
                pivot_pos = -1
            else:
                pivot_pos = 0
    
        partitioned, pivot_pos = partition(array, pivot_pos)
        left_sorted, left_com = quick_sort(args, partitioned[:pivot_pos])
        right_sorted, right_com = quick_sort(args, partitioned[pivot_pos+1:])

        return left_sorted+[partitioned[pivot_pos]]+right_sorted, l+left_com+right_com-1

parser = argparse.ArgumentParser(description='Quick Sort Algorithm')
parser.add_argument('--file_path', type=str, default='test.txt',
                    help='Path of file where unsorted array is stored')
parser.add_argument('--pivot', choices=["first", "last", "median"], default='first', 
                    help='How pivot should be selected')

args = parser.parse_args()

filename = args.file_path
input_array = []

lines = open(filename,'r').readlines()
for num in lines:
    input_array.append(int(num.strip('\n')))

sorted_array, num_com = quick_sort(args, input_array)

if sorted(sorted_array) == sorted_array:
    print('Correct!')
    print(num_com)
