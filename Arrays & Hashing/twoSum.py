nums = [3,2,4]
target = 6

# def twoSum(nums, target): #time complexity == o(n^2)
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return False

# print(twoSum(nums, target))

# Better solution with extra memory

def twoSum(nums, target):
    prevMap = dict() # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [i, prevMap[diff]]

        prevMap[n] = i
    return False

print(twoSum(nums, target))

