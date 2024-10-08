# Declare variables
nums = [3, 2, 5, 1, 4]  # Example list of numbers


def bubblesort1(nums):
    temp = 0
    loops = 0
    swap = False 
    while not swap:
        swap = False
        for pos in range(1, len(nums)):
            loops += 1
            if nums[pos - 1] > nums[pos]:
                temp = nums[pos - 1]
                nums[pos - 1] = nums[pos]
                nums[pos] = temp
                swap = True
        print(loops)
        return nums


def bubblesort2(nums):
    # Declare variables
    nums = [3, 2, 5, 1, 4]  # Example list of numbers
    loops = 0
    # Bubble Sort Algorithm
    for i in range(len(nums)):
        swap = False
        for pos in range(1, len(nums) - i):
            loops += 1
            if nums[pos - 1] > nums[pos]:
                nums[pos - 1], nums[pos] = nums[pos], nums[pos - 1]  # Swap
                swap = True
        if swap == False:
            break
        print(loops)
        return nums

        
def optimized_bubble_sort(nums):
    n = len(nums)
    loops = 0
    for i in range(n):
        swapped = False
        for j in range(1, n - i):
            loops += 1
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]  # Swap
                swapped = True
        if swapped == False:
            break
    print(loops)
    return nums

nums = [3, 2, 5, 1, 4]
print(optimized_bubble_sort(nums))
print(bubblesort1(nums))
print(bubblesort2(nums))
