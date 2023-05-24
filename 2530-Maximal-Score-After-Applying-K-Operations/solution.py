class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0 # var to store the score
        nums = [-i for i in nums] # making all values negative cuz we will heapify
        heapify(nums) # heap defaults to min heap, so we make nums negative
        while k: # k = number of iterations
            curr = -1 * heapq.heappop(nums) # pop the 'smallest' num, but in reality it is the largest num when positive
            score += curr # add the max
            curr = -1 * math.ceil(curr/3) # use the ceil function as it sasy in the question
            heappush(nums, curr) # put the num back in the heap using heappush
            k-= 1 # dont forget, otherwise it will become an infinite loop
        return score # return the value!
