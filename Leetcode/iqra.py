"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

s = "aba"
Output => True

"""

s="cardrac"
Output = True

s = "abca"
Output = True

#first step: check if palindrome 



# the remaining letter must match

def is_palindrome(s):
	#insert into stack until you run into a repetitive letter
  in_stack = []
  stacked = stack()
  i=0
  while (s not in in_stack):
  	stacked.append(s[i])
    i += 1
  
  #pop from stack
  j = 0
	while(not stacked.empty()):
  	char = stacked.pop()
    if (char != s[i] and j!=0):
    	return False
		j+= 1
  return True

s="cardrac"
in_stack = [c, a, r, d]
i = 4

i = 5
j = 0
char = d

j = 1
char = r

j = 2
char = a 


j= 3
char = c

retur True



  

#if not - see if a deleting a letter










#
"""
Given an array nums of distinct integers, return all the possible 
permutations
. You can return the answer in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

def permutations(nums):
  # component for loop
  results = []
  for (i in range(factorial(len(nums))):
       sub_array = []
       results.append(sub_array)
      
  for (num in nums):
       
  []
  [1]
  [1,2]
  [1,2,3]
       
    
  # position
