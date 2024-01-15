# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:45:45 2024

@author: benib

Write a program that displays all the lower-case consonants of the alphabet in alphabetical order, separated by spaces.
"""
for ascii in range(ord('a'), ord('z') + 1):
    if not((ascii == ord("a")) or (ascii == ord("e")) or (ascii == ord("i")) or (ascii == ord("o")) or (ascii == ord("u")) or (ascii == ord("y"))) :
        print(chr(ascii), end = " ")
