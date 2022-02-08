#!/usr/bin/env python

import sys


def calcu_mean(nums):
    sum1 = 0
    for i in nums:
        sum1 = sum1 + int(i)
    mean = sum1/len(nums)
    print('The mean of these numbers is:',mean)
       
def calcu_mode(nums):            
    from collections import Counter    
    median_list = Counter(nums).most_common()     
    standard=median_list[0][1]  
    li=[]
    for i in median_list:
        if i[1] == standard:
            li.append(i[0])    
        else:
            continue
    print('the mode of these numbers is(are)',li)
        
def calcu_median(nums):
    sorted_nums = sorted(nums, reverse=False)
    len_num = len(nums)
    if len_num%2 == 0:
        median = (int(sorted_nums[int(len_num/2)-1])+int(sorted_nums[int(len_num/2+1)-1]))/2
        print('The median of these numbers is:',median)
    else:
        median = sorted_nums[int((len_num-1)/2)]
        print('The median of these numbers is:',median)

def main(args):
    ex_mean = args.__contains__('--mean')
    ex_median = args.__contains__('--median')
    ex_mode = args.__contains__('--mode')
    if ex_mean == True and ex_median == True and ex_mode == False:
        if len(args) <= 10:
            new_args=[int(i) for i in args[2:] ]
            calcu_mean(new_args)
            calcu_median(new_args)
        else:
            print('error, 8 and less numbers are expected')
    elif ex_mean == True and ex_median == False and ex_mode == True:
        if len(args) <= 10:
            new_args=[int(i) for i in args[2:] ]
            calcu_mean(new_args)
            calcu_mode(new_args)
        else:
            print('error, 8 and less numbers are expected')
    elif ex_mean == False and ex_median == True and ex_mode == True:
        if len(args) <= 10:
            new_args=[int(i) for i in args[2:] ]
            calcu_median(new_args)
            calcu_mode(new_args)
        else:
            print('error, 8 and less numbers are expected')
    elif ex_mean == True and ex_median == False and ex_mode == False:
        if len(args) <= 9:
            new_args=[int(i) for i in args[1:] ]
            calcu_mean()
        else:
            print('error, 8 and less numbers are expected')
    elif ex_mean == False and ex_median == True and ex_mode == False:
        if len(args) <= 9:
            new_args=[int(i) for i in args[1:] ]
            calcu_median(new_args)
        else:
            print('error, 8 and less numbers are expected')
    elif ex_mean == False and ex_median == False and ex_mode == True:
        if len(args) <= 9:
            new_args=[int(i) for i in args[1:] ]
            calcu_mode(new_args)
        else:
            print('error, 8 and less numbers are expected')
    if ex_mean == False and ex_median == False and ex_mode == False:
        if len(args) <= 8:
            calcu_mean(args)
            calcu_median(args)
            calcu_mode(args)
        else:
            print('error, 8 and less numbers are expected')
        
 
if __name__ == '__main__':
    main(sys.argv[1:])