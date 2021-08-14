#!/usr/bin/python3.9
# -*- coding -*-

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

  # override str
  def __str__(self):
    curr_point = self
    format_str="("
    while(curr_point):
      format_str += str(curr_point.val)
      if curr_point.next is None:
        format_str += ")"
      else :
        format_str += " -> "
      curr_point = curr_point.next
    return format_str


class Solution:

  # convert a ListNode to a number
  def toNumber(self, lstn):
    currentPoint = lstn
    currVal = 0
    valuer = 1
    while(currentPoint):
      currVal += currentPoint.val * valuer
      valuer *= 10
      currentPoint = currentPoint.next
    return currVal

  def addTwoNumbers(self, l1, l2, c = 0):
    resultL = None
    resultPointer = None
    carry = 0

    pointer1 = l1
    pointer2 = l2

    while (pointer1 or pointer2):
      # get value 
      val1 = pointer1.val if pointer1 else 0
      val2 = pointer2.val if pointer2 else 0
      # add individual digits
      result_sum = val1 + val2 + carry
      # comprobe state of the add result 
      if result_sum > 9:
        result_sum %=10
        carry=1
      else:
        carry =0
      # save the pointer
      if resultPointer:
        resultPointer.next = ListNode(result_sum)
        resultPointer = resultPointer.next
      else:
        resultL = ListNode(result_sum)
        resultPointer = resultL
      # Recover the pointers 
      pointer1 = pointer1.next if pointer1 else None
      pointer2 = pointer2.next if pointer2 else None

    return resultL


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)

print(l1)
print(l2)
print(result)
#while result:
#  print result.val,
#  result = result.next

# 7 0 8
