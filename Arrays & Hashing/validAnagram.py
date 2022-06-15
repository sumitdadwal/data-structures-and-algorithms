from random import randrange


s = "nagaram"
t = "anagram"

# def validAnagram(s, t):   time complexity, space complexity #O(n)
#     if len(s) > len(t) or len(s) < len(t):
#         return False
#     sCount = dict()
#     tCount = dict()

#     for i in range(len(s)):
#         if s[i] in sCount:
#             sCount[s[i]] += 1
#         else:
#             sCount[s[i]] = 1
    
#     for j in range(len(t)):
#         if t[j] in tCount:
#             tCount[t[j]] += 1
#         else:
#             tCount[t[j]] = 1
#     print(sCount, tCount)

#     for c in sCount:
#         if sCount[c] != tCount.get(c, 0):
#             return False
#     return True



# print(validAnagram(s, t))

def isAnagram(s, t): #space complexity = O(1)
    return sorted(s) == sorted(t)
print(isAnagram(s, t))

# good sorting algorithms do use extra memory o(nlogn) atleast but 
# in most interviews we assume that sorting in O(1) so this something to clarify with
# the interviewer.
