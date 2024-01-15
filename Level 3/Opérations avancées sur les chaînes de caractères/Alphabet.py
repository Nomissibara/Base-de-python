# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:41:58 2024

@author: benib

Write a program that displays all the characters of the alphabet in uppercase, with a space between each character.

We'll use a loop, of course!
"""
for ascii in range(ord('A'), ord('Z') + 1):
    print(chr(ascii), end = " ")
