#/usr/bin/python3
#-*- coding: utf-8 -*-


class Solution:
  def lengthOfLongestDistSubstring(self, s, k):
    lngthDistSbStr=0

    for indx in range(0,len(s)):
      currentDists = 0
      tmpSubstr = ''
      for character in s[indx:]:
        if character in tmpSubstr:
          tmpSubstr += character
        else:
          currentDists +=1
          if currentDists > k:
            tmpLen = len(tmpSubstr)
            lngthDistSbStr = lngthDistSbStr if lngthDistSbStr > tmpLen else tmpLen
          else:
            tmpSubstr += character

    return lngthDistSbStr


print(Solution().lengthOfLongestDistSubstring('abcba',2))





