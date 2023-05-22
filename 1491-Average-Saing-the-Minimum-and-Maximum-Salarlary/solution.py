class Solution:
    def average(self, salary: List[int]) -> float:
        av = 0.0 # make float variable av for average
        for i in salary:
            av += i # get the sum of all elements

        return (av -min(salary) - max(salary))/(len(salary) -2) # substract the min and max value in the list. decrease length by 2
