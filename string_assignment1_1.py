# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:44:17 2020

@author: SATHWIK
"""


test_str= "gitamuniversity"
all_freq= {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("count of all characters in string is ;\n:"+str(all_freq))