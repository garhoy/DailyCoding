'''
Given a string, find the length of the longest substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        vector = ""
        count = 0
        maxcount = 0
        
        for i in s:
            if i in vector:
                vector = ""
                count = 0
            else:
                vector += i 
                count +=1

            if maxcount < count: 
                maxcount = count
        return maxcount


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
