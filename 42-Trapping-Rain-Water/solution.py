class Solution:
    def trap(self, h: List[int]) -> int:

        water = 0 # var to store the amount of water
        if max(h) == min(h): # this is to increase efficiency for an edge case. [1]*(10**4). If the min and max are equal then water trapped = 0
            return  0
        for i in range(1, len(h)-1): # not considering the first and last spot as no water can be stored there
            temp = min(max(h[:i]), max(h[i+1:])) - h[i] # this is store the value of water possible
            if temp > 0: # only add it if it nets out to be positive
                water += temp 
        return water # return!

# this problem took a while, these are the two solutions i tried before getting to the correct one.
