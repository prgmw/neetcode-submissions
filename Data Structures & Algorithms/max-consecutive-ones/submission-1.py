class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        resp = 0
        aux = 0
        for item in nums:
            if item == 1:
                aux = aux + 1
                if aux > resp:
                    resp = aux
            else:
                aux = 0
        return resp