from pyparsing import alphanums


s = 'race a car'

# def isPalindrome(s): #cheating solution. using built in functions and extra memory
#     newStr = ""

#     for c in s:
#         if c.isalnum():
#             newStr += c.lower()
#     print(newStr)
#     return newStr == newStr[::-1]
        

# print(isPalindrome(s))

class Solution:
    def isPalindrome(self, s): #better solutuon because no extra memory used
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


    def alphaNum(self, c):
        return (ord('A') <= ord(c) <=ord('Z') or
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
                

sol = Solution()
print(sol.isPalindrome(s))
    
    

