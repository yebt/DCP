 #/usr/bin/python3
 # -*- coding: utf8 -*- 

class Solution:
  def lengthOfLongestSubstring(self, s):
    lgstSize = 0
    tmpSubString = ''
    for character in s:
      if character in  tmpSubString:
        tmpSize = len(tmpSubString)
        if lgstSize < tmpSize:
          lgstSize = tmpSize
        tmpSubString=character
      else:
        tmpSubString+=character

    return lgstSize

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
