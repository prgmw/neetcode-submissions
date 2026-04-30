class Solution:

    def climbStairs(self, n: int) -> int:
        #if n <= 1:
         #   return 1

        #return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        if n == 1:
            return 1
        
        aux0 = 1
        aux1 = 1
        acc = 0

        for itr in range(n -1):
            acc = aux0 + aux1
            
            aux0 = aux1
            aux1 = acc
        
        return acc
        