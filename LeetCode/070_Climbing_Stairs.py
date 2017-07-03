class Solution(object):
    def climbStairs(self, n):
        one_step_before = 2
        two_steps_before = 1
        if n == two_steps_before or n == one_step_before:
            return n
        
        for i in range(2,n):
            final = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = final
        return one_step_before

        