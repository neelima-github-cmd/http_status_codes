# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:50:26 2020

@author: Neelima Sunku
"""

#Python program to generate password

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

all = lower+upper+numbers+symbols
length_16 = 16
length_8 = 8
password = "".join(random.sample(all,length_16))
print(password)