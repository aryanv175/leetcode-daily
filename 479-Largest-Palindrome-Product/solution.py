class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n== 1: # case if n = 1
            return 9
        upper = (10 ** n) -1 # for everything else. easy to cacluate upper and lower bound values.
        lower = 10 ** (n-1)
        res = 0 # the variable to store our result

        for i in range(upper, lower-1, -2): # we only need odd elements (increment= -2), as the first digit of the largest pallindrome will be 9
                                            # so the last digit should be 9 also. no even numbers multiplied will give 9 in the unit's place.
            if i * i < res:
                return res%1337  # if our current res is bigger than the biggest number possible for the next iteration, we can simply returnt the
                                 # current res.
            for j in range(upper, i-1, -2):
                temp = i* j
                if temp % 11 != 0 and temp > res: # all even numbered digit pallinfomes are multiples of 11
                    continue
                if (str(temp)[::-1] == str(temp)): # make sure it is a pallindrome
                    res = temp
                

        return res%1337 # return!
