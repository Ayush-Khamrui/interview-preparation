# Write a program to reverse an array or string
# Difficulty Level : Basic
# Date : 11th July, 2021
 
# Given an array (or string), the task is to reverse the array/string.
# Examples : 
 
# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}

def reverseList(arr):
    print(arr[::-1])
arr = [4, 5, 1, 2]
reverseList(arr)