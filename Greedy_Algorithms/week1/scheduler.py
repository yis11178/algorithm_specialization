'''
Script to schedule jobs with specified importance (weight)
and time to finish (length),
using Greedy algorithm.

Sorting algorithms are not implemented here and 
built-in function is used instead.
'''

import sys

filename = sys.argv[1]
jobs = []

lines = open(filename,'r').readlines()
for line in lines[1:]:
    w, l = line.strip().split(' ')
    w = int(w)
    l = int(l)
    diff = w - l
    ratio = w/l
    jobs += [[w, l, diff, ratio]]

def calc_time(job_list):
    # Calculate weighted completion time
    completion_time = 0
    sum = 0
    for job in job_list:
        w, l = job[:2]
        completion_time += l
        sum += w*completion_time
    return sum

# Obtain ordering based on weight - length
jobs.sort(key=lambda x:(x[2], x[0]), reverse=True)
print('Sum of weighted completion time ordered by difference: ',
        calc_time(jobs))

jobs.sort(key=lambda x:x[-1], reverse=True)
print('Sum of weighted completion time ordered by ratio: ',
        calc_time(jobs))