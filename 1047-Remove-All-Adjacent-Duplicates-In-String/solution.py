class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [] # solving this problem using stack
        for char in s: # iterate thorugh every character in string s
            if len(stack) != 0: # if the len of stack is 0 then stack[-1] will give an error 
                if char == stack[-1]: # if the element is repeated, we pop it
                    stack.pop()
                else:
                    stack.append(char) # otherwise we put it in the stack
            else: # if the stack is empty we put the current char in the stack
                stack.append(char)
        return ''.join(stack) # join the stack list using the join operand.
