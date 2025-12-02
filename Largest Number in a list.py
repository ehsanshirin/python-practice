# The largest number in a list.

nums = list (map (int ,input ('type multiple number, with space: ').split()))
nums.sort()
print(nums[-1])


# The largest number in a list with max.

nums = list(map(int, input('Type multiple numbers, separated by spaces: ').split()))
print(f'The largest number is {max(nums)}')