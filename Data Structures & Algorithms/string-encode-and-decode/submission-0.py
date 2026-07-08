"""
ENCODE
Input is list of strings
ex: ["hello", "world"]
output is a single string with delimeters 
ex: "5#hello5#world"


"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Loop through list and build the string with delimeters
        # The delimeter will have a number to inform how long string is, and then # to know where to start
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        # Split encoded string into list of individual words
        res = [] # holds individual words
        i = 0 # starting point
        while i < len(s): 
            j = s.find("#", i) # will have index of #
            length = int(s[i:j])
            start_parse = j + 1
            end_parse = start_parse + length
            sub = s[start_parse:end_parse]
            res.append(sub)
            i = end_parse
        
        return res

