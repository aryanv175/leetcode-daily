class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2 # get a new array with all the arrays
        res.sort() # sort the array
        if len(res) % 2 == 0: # if len of array is even then median is the average of the two middle elements
            return (res[len(res)//2] + res[(len(res)//2) -1] ) /2
        return res[len(res)//2] # if lem of array is  odd then median is the middle element
