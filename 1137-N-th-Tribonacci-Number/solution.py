class Solution:
    def tribonacci(self, n: int) -> int:
        # initialising the values t0, t1, t2
        t0 = 0 
        t1= t2 = 1
        res = t0 + t1 + t2

        # edge cases when n < 3.
        if n == 0:
            return t0
        elif n==1:
            return t1
        elif n == 2:
            return t2
        
        # we use a for loop to get the value of the tribonacci number
        while n -3  > 0:
            t0 = t1
            t1 = t2
            t2 = res
            res = t0 + t1 + t2
            n -= 1

        return res # return!
