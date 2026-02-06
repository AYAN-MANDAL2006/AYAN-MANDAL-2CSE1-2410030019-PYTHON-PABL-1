"""Given an array arr[]. Your task is to find the minimum and maximum elements 
in the array.
Examples:
Input: arr[] = [1, 4, 3, 5, 8, 6]
Output: [1, 8]
Explanation: minimum and maximum elements of array are 1 and 8."""

class Solution:
    def getMinMax(self, arr):
        mn = mx = arr[0]
        for x in arr:
            if x < mn: mn = x
            if x > mx: mx = x
        return mn, mx
