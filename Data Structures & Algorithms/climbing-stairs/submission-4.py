class Solution:

    def climbStairs(self, n: int) -> int:
        #if n <= 1:
         #   return 1

        #return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        if n <= 2:
            return n
        
        prev = 1
        curr = 1
        acc = 0

        for itr in range(n -1):
            acc = prev + curr
            
            prev = curr
            curr = acc
        
        return acc
        