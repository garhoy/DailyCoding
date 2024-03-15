'''
A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
'''

class Solution:
    def longestPalindrome(self, s) -> str:
        if not s:
            return ""

        longestpal = s[0]  

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]  
                #print(substring)
                
                if substring == substring[::-1]:  
                    if len(substring) > len(longestpal): 
                        longestpal = substring

        if len(longestpal) < 3:
            return ""
        return longestpal

# Test program
s = "tracecars"
print(Solution().longestPalindrome(s))
s = "weca"
print(Solution().longestPalindrome(s))
s = "Banana"
print(Solution().longestPalindrome(s))
s = "million"
print(Solution().longestPalindrome(s))
s = "winchcniw"
print(Solution().longestPalindrome(s))
