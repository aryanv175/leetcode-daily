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

        '''water = 0
        curr = 0
        while curr < len(h)-2:
            nex = curr+2
            if h[curr] == 0 or nex == len(h):
                curr += 1 
                continue
            if h[curr] > max(h[curr+1:]):
                if h[curr+1] < max(h[curr+2:]):
                    while h[curr+1] > h[nex] and nex < len(h):
                        nex+= 1
                    water += (nex - curr - 1)*min(h[curr], h[nex])
                    for i in range(curr+1, nex):
                        water -= h[i]
                    curr = nex 
                    continue
                else:
                    curr+= 1
                    continue
            while h[curr] > h[nex]:
                nex+= 1      
            water += (nex - curr - 1)*min(h[curr], h[nex])
            for i in range(curr+1, nex):
                water -= h[i]
            curr = nex
            print(water)
        if water<0:
            return 0
        return water
        water = 0
        curr = 1
        while curr < len(h) - 2:
            nex = curr + 2

            if h[curr] < h[curr + 1] or h[curr + 1]> h[nex]:
                curr += 1
                continue
            water += min(h[curr], h[nex]) - h[curr + 1]
            print(h[curr], h[nex], water)
            curr = nex
        return water'''
        
