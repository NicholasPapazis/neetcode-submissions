"""
nums = [1, 2, 3, 4, 5]

Iteration 1
i = 0
val = 1
target = 7
complement = 6

"""

"""
create map (key is number, value is its index)
iterate through nums
calculate complement
if complement is in map
    return current index and value of the complement stored in the map
outside iteration, return False

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Creat map
        map = {}

        # Iterate through nums
        for i, val in enumerate(nums): 

            # If Target - current num in nums
            complement = target - val
            if complement in map:

                # return the tuple of indecies
                return [map[complement], i]
            
            # If complement is not in map, add current value to map with correct index  
            map[val] = i


        