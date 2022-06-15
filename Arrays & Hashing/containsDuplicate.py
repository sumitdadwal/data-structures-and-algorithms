nums = [1,2,3,4,5,6,1]

# def containsDuplicate(nums):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False

# print(containsDuplicate(nums))

# BETTER SOLUTION BUT MEMORY IS HIGH

def containsDuplicate(nums):
    d = dict()

    for i in range(len(nums)):
        print(d)
        if nums[i] in d:
            return True
        else:
            d[i] = nums[i]
    print(d)
    return False

print(containsDuplicate(nums))

