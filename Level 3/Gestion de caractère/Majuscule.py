# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 23:18:44 2024

@author: benib

Write a program that reads a line of text from the keyboard and displays the contents of this line, transforming all lower-case characters it contains into uppercase, and redisplaying the remaining characters as-is.

CONSTRAINTS :
The line contains no more than 10,000 characters.

It contains no accented characters.
"""
line_of_text = input()
print(line_of_text.upper())
