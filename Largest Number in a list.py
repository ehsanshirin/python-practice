# The largest number in a list.

nums = list (map (int ,input ('type multiple number, with space: ').split()))
nums.sort()
print(nums[-1])
