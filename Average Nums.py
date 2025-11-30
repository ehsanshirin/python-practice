try:
    nums = list(map(float, input('Type multiple numbers, separated by spaces: ').split()))
    if nums:
        print(f'Average of your numbers is {sum(nums) / len(nums):.2f}')
    else:
        print('No numbers entered.')
except ValueError:
    print('Please enter valid numbers only.')