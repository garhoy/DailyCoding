'''
Given a string, find the length of the longest substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIndexMap = {}
        start = 0
        maxLength = 0
        
        for i, char in enumerate(s):
            # If char is in the current substring
            print(i,char,charIndexMap)
            if char in charIndexMap and charIndexMap[char] >= start:
                start = charIndexMap[char] + 1  # Move start right after the last occurrence of char
            else:
                maxLength = max(maxLength, i - start + 1)  # Update maxLength if we found a longer substring
            
            charIndexMap[char] = i  # Update the last seen index of char
            
        return maxLength



print(Solution().lengthOfLongestSubstring('tmmzuxt'))
