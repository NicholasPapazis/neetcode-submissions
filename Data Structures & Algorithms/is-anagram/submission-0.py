"""
"cat" and "tac" and "act" are anagrams
Must have same length, same number of each character
"""

"""
Plan: increment/decrement values of corresponding to keys in map. 
Key will be the character
Value will be its frequency
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if s and t are different lengths
        if len(s) != len(t):

            # Return false 
            return False

        # Create a map
        map = {}

        # Iterate over s
        for ch in s:

            # one line of python code that adds element to map with value of 0 if not already, then increments it value
            map[ch] = map.get(ch, 0) + 1

        # Iterate over t
        for ch in t: 

            # one line of python code that adds element to map with value of 0 if not already, then decrements it value
            map[ch] = map.get(ch, 0) - 1

        # if all values in map equal 0
        if all(v == 0 for v in map.values()):

            # return True
            return True
        
        # return False
        return False
            