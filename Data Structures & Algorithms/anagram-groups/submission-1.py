"""
Figure out which elements in input have same frequency map.

hash map (key is sorted anagram, value is array of the anagrams)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create hash map
        map = {}

        # Iterate thgrough strs
        for i in strs:

            # Sort strs
            sorted_i = "".join(sorted(i))

            # If str does not exist in hashmap
            if sorted_i not in map:

                # Create an empty list for the str
                map[sorted_i] = []
            
            # add str to list
            map[sorted_i].append(i)

        # return all lists
        return list(map.values())

            
        