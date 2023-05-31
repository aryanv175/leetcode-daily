class Solution:
    def maxArea(self, height: List[int]) -> int:
        # using two pointers. we move the pointer which has the lesser value = height[pointer]
        left = 0 # left pointer at the start
        right = len(height) - 1 # right pointer in the end
        water = (right - left) * min(height[left], height[right]) # water to start with, this is also good for the edfe case with only 2 elements
        while left < right: # we do this until the left and right pointer coincides
            if height[left] < height[right]: # as discussed before we move the pointer which has right value
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else: # if they are equal, then we check the next values of each pointer and move to the larger one
                if height[left+1] > height[right-1]:
                    left += 1
                elif height[left+1] < height[right-1]:
                    right -=1
                else:
                    left+= 1 # if those are also equal just do either one. Left += 1 or right -= 1. does not matter.
            
            if water < (right - left) * min(height[left], height[right]): #  only replace the water value if the new value is more
                water  = (right - left) * min(height[left], height[right])
        return water # return water!
