"""
Frequency map of elements
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create frequency map
        map = {}

        # iterate through nums
        for i in nums:

            # if current item not in map, add it with value of 0
            # increment current item value by 1
            map[i] = map.get(i, 0) + 1

        # sort map in descending order by value
        sorted_map = sorted(map.items(), key=lambda x: x[1], reverse=True)

        # return the top k elements of the sorted map
        top_k_keys = [k for k, v in sorted_map[:k]]

        return top_k_keys






