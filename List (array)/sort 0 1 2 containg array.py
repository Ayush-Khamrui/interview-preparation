# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order. 
# Difficult: Easy
# Date: 11th July, 2021

# Example 1:

# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.
# Example 2:

# Input: 
# N = 3
# arr[] = {0 1 0}
# Output:
# 0 0 1
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= N <= 10^6
# 0 <= A[i] <= 2
def sort012(self,arr,n):
    a = {i:arr.count(i) for i in arr}
    b = []
    if 0 in a.keys():
        b+=[0]*a[0]
    if 1 in a.keys():
        b+=[1]*a[1]
    if 2 in a.keys():
        b+=[2]*a[2]
    for i in range(n):
        arr[i] = b[i] 

        