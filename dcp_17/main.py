#/usr/bin/python3
#-*- coding: utf-8 -*-

class Solution:
  def longestAbsolutePath(self,s):
    absPaths=[]
    absLengthsPaths=[]
    lngestPath = 0
    lngestPathstr = ''

    listPaths = s.split('\n')
    # work on stacks
    for path in listPaths:
      levelDeep = path.count('\t')
      lenAbsPath = len(absPaths)
      strPath = path[levelDeep:]

      # concatr path 
      if lenAbsPath > levelDeep and lenAbsPath != 0:
        absPaths = absPaths[:lenAbsPath-1]
        absLengthsPaths = absLengthsPaths[:lenAbsPath-1]
      absPaths.append(strPath)
      absLengthsPaths.append(len(strPath))

      #probe if is a file
      if '.' in strPath:
        tmpPathLength =0
        tmpPathStr = ''
        for indx in range(len(absPaths)):
          tmpPathLength += absLengthsPaths[indx]
          tmpPathStr += absPaths[indx]
          if indx != len(absPaths)-1:
            tmpPathLength +=1
            tmpPathStr+='/'
        if lngestPath < tmpPathLength:
          lngestPath = tmpPathLength
          lngestPathstr = tmpPathStr

    print(lngestPathstr)
    return lngestPath


print(Solution().longestAbsolutePath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
print(Solution().longestAbsolutePath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))

"""
dir\n\tsubd1\n\t\tfile1.ext\n\tsubd2\n\tsubd3\n\t\tfile2.ext\n\t\tfile3.ext
"""
