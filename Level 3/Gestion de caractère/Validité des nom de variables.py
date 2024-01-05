# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 21:26:13 2024

@author: benib

CONSTRAINTS
    The length of each proposed name will not exceed 100 characters.

INPUT
    The first line contains the integer nbNames. The following nbNames lines each contain one possible variable name.

    None of the possible variable names will be a language keyword. So you don't have to worry about them.

OUTPUT
    You must display nbLineNames on the output, indicating in the order in which they are given as input, whether the names proposed are valid.

    Display the text "YES" for a valid identifier and "NO" for an invalid identifier.
"""

nbNames = int(input())
for loop in range(nbNames):
    name_of_variable = input()
    start = 0
    end = len(name_of_variable) - 1
    check = True
    if not(("a" <= name_of_variable[start] and name_of_variable[start] <= "z") or ("A" <= name_of_variable[start] and name_of_variable[start] <= "Z") or (name_of_variable[start] == "_")):
        check = False
    else :
        while start < len(name_of_variable):
            if not(("a" <= name_of_variable[start] and name_of_variable[start] <= "z") or ("A" <= name_of_variable[start] and name_of_variable[start] <= "Z") or (name_of_variable[start] == "_") or ("0" <= name_of_variable[start] and name_of_variable[start] <= "9")) :
                check = False
            start += 1
            end -=1
    if check :
        print("YES")
    else :
        print("NO")