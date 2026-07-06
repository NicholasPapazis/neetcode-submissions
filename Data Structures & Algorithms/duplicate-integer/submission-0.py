"""
A list,
check if element is in list,
if is in list
return true
if not in list
add it to list
if entire list traversed
return false
"""

"""

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create list
        int_array = []

        #iterate through nums
        for i in nums: 
            
            # if current element is in list
            if i in int_array: 
                
                # return true
                return True

            # add current element to list
            int_array.append(i)
        
        # return false
        return False

"""
we return false outside the iteration on int_array because the only way we exit that 
loop is by not finding a duplicate. 
"""





        