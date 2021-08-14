#/usr/bin/python3
#-*- coding: utf-8 -*-

class Solution:
  def maxK(self,arr,k):
    for i in range(len(arr)-k+1):
      currMax = arr[i]
      for j in range(1,k):
        if arr[i+j] > currMax:
          currMax = arr[i+j]

      print(currMax, end=' ')

Solution().maxK([10, 5, 2, 7, 8, 7],3)



