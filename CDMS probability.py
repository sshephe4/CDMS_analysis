#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 11:22:37 2026

@author: sammisheps
"""

import numpy as np
import matplotlib.pyplot as plt


#let's take some protein with a distribution across 4 charge states 
#10% for an 11+, 40% for a 12+, 30% for a 13+, and 20% for a 14+

mz10=0.001
mz11=0.099
mz12=0.4
mz13=0.3
mz14=0.2





mz10_list_sum=[]
mz11_list_sum=[]
mz12_list_sum=[]
mz13_list_sum=[]
mz14_list_sum=[]


# for some set of ions [x] there is a 10% probability that any given ion is mz11

#have it 'choose' x number of ions where if the random number is between 0 and 0.1 it is mz11
# between 0.1 and 0.5 mz12; 0.5 to 0.8 mz13; and 0.8 to 1 mz14

avg_num=1000
for k in range(avg_num):
    mz10_list_counts=[]
    mz11_list_counts=[]
    mz12_list_counts=[]
    mz13_list_counts=[]
    mz14_list_counts=[]
    num_ions=10
    repeats=10
    for j in range(repeats):
        ion_list=np.random.rand(num_ions)

        
        mz10_res = len([i for i in ion_list if i < 0.001])
        mz10_list_counts.append(mz10_res)
        mz10_avg_rnd1=np.average(mz10_list_counts)/num_ions
        mz11_res = len([i for i in ion_list if i > 0.001 and i < 0.1])
        mz11_list_counts.append(mz11_res)
        mz11_avg_rnd1=np.average(mz11_list_counts)/num_ions
        mz12_res = len([i for i in ion_list if i > 0.1 and i < 0.5])
        mz12_list_counts.append(mz12_res)
        mz12_avg_rnd1=np.average(mz12_list_counts)/num_ions
        mz13_res = len([i for i in ion_list if i > 0.5 and i < 0.8])
        mz13_list_counts.append(mz13_res)
        mz13_avg_rnd1=np.average(mz13_list_counts)/num_ions
        mz14_res = len([i for i in ion_list if i > 0.8 and i < 1])
        mz14_list_counts.append(mz14_res)
        mz14_avg_rnd1=np.average(mz14_list_counts)/num_ions

    print(k)
    mz10_list_sum.append(mz10_avg_rnd1)
    mz11_list_sum.append(mz11_avg_rnd1)
    mz12_list_sum.append(mz12_avg_rnd1)
    mz13_list_sum.append(mz13_avg_rnd1)
    mz14_list_sum.append(mz14_avg_rnd1)


final_sum_10=np.average(mz10_list_sum)
final_sum_11=np.average(mz11_list_sum)
final_sum_12=np.average(mz12_list_sum)
final_sum_13=np.average(mz13_list_sum)
final_sum_14=np.average(mz14_list_sum)


print(final_sum_10,final_sum_11,final_sum_12,final_sum_13,final_sum_14)
    
