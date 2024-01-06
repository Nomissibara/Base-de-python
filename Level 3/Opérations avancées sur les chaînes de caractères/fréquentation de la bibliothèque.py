# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:24:10 2024

@author: benib

INPUT
    An unknown number of lines, each containing an unknown number of integers, the number varying from line to line.

    The integers are separated by a single space, and there are no spaces at the end of the line.

OUTPUT
    You must indicate the sum of all integers.
"""


check = False
sum_of_integer = 0
while not check:
   try:
      days = input()
   except:
      check = True
   if not check:
      for nb in map(int, days.split(" ")):
         sum_of_integer += nb
print(sum_of_integer)