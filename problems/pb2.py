# In pb2.py, create a function that given a list of numbers (positive or negative integers),
# it will return a list containing the indices of the two highest values. Order of the returned indices does not matter.

def max_values(nums):
    # Initialize float variable to hold max value
    max = float('-inf')

    # Iterate through numbers
    for num in nums:
        # Check for greater values
        if num > max:
            # Set those values into a new variable
            max = nums

    return max

# print(max_values([4, 7, 2, 8, 10, 9])) # -> [4, 5]
# print(max_values([-5, -2, -1, -11])) # -> [1, 2]
