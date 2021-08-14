#/usr/bin/python3
#-*- coding: utf-8 -*-

class Solution:
  def minCost(self,costsArr):
    # set vars vars indicate size and set validat
    # componet 
    iColors = len(costsArr)
    if iColors == 0:
      return 0

    nHouses = len(costsArr[0])
    if nHouses == 0:
      return 0

    # create dependeces arr
    # fill of 0's
    dp = [[0 for i in range(nHouses)] for j in range(iColors)]
    #dp = [[0] * nHouses]* iColors
    print(dp)

    # get the base cost
    for i in range(iColors):
      dp[i][0] = costsArr[i][0]

    # init in i in 1, couses 0 cost now is get
    for i in range(1,nHouses):
      columnDp = [row[i-1] for row in dp]
      for j in range(iColors):
        dp[j][i] = min(x for k,x in enumerate(columnDp) if k != j) + costsArr[j][i]

    print(dp)
    return(min([row[nHouses-1] for row in dp] ))


#print(Solution().minCost( [[14,2,11],[11,14,5],[14,3,10],[4,12,7]]))
print(Solution().minCost( [[14,2,11],[11,14,5],[14,3,10]]))


