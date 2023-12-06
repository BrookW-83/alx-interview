#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    
    copied_chars = 1  
    clipboard = 0     
    operations = 0    
 
    while copied_chars < n:
       
        if clipboard == 0:
            clipboard = copied_chars  
            operations += 1  

     
        if copied_chars == 1:
            copied_chars += clipboard 
            operations += 1  
            continue

        remaining = n - copied_chars  

        if remaining < clipboard:
            return 0

       
        if remaining % copied_chars != 0:
            copied_chars += clipboard  
            operations += 1 
        else:
            clipboard = copied_chars 
            copied_chars += clipboard 
            operations += 2  

    
    if copied_chars == n:
        return operations
    else:
        return 0
    
'''
Calculates the fewest number of operations
    needed to result in exactly n H
    characters in this file.

    Args:
        n (int): The desired number of characters.

    Returns:
        int: The minimum number of operations needed.
             Returns 0 if n is impossible to achieve.
'''