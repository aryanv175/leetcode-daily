class Solution:
    def greatestLetter(self, s: str) -> str:
        res = '' # char to store our result
        for char in s: # iterate through the string. Check if the upper and lower of that char are present in the string
            if (char.upper() in s and char.lower() in s) and char.upper() > res: # and if that char is bigger than our current maximum.
                res = char.upper() # if so, update the result.
        return res # return!
      
# how did i come up w two solutions that are so different like literally one after the other? Not commenting the second one lol

"""class Solution:
    def greatestLetter(self, s: str) -> str:
        temp = s # copy of original string as we are about to
        s = s.lower() # lowercase it
        multiple = [] # list to store chars that could be our answer. 
        freq = defaultdict(lambda: 0) # default dict to store the frequency of each 
        for char in s:
            freq[char] += 1
        for char in freq.keys():
            if freq[char] > 1 and (char.upper() in temp and char in temp):
                multiple.append(char.upper())
        
        if len(multiple) == 0:
            return ''
        res = 'A'
        for i in range(len(multiple)):
            if multiple[i] > res:
                res = multiple[i]
        return res
"""
