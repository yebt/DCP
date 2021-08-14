#/usr/bin/python3
#-*- coding: utf-8 -*-

import random

class Solution:
  def estimatePy(self):
    # suppose that the circle's radius is 1
    # so the range of the numbers in the circle is 
    # [0.0, 1.0)

    error = 0.00000001
    currentAprx = 0
    nPoints = 0
    nPointsInside = 0
    random.seed(10)
    while(True):
      x = random.random()
      y = random.random()
      if (x*x + y*y ) < 1:
        nPointsInside +=1
      nPoints += 1

      prevAprx = currentAprx
      currentAprx = (nPointsInside / nPoints)
      absError = abs(currentAprx - prevAprx)
      print(currentAprx*4)
      if ( absError < error and absError != 0 ):
        break

    return currentAprx*4


print (Solution().estimatePy())




