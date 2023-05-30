class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums])
        # square all the numbers using for loop
        # use the sorted function to sort them!
