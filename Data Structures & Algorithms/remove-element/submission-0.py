class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #aux = set(nums)
        #aux.remove(val)
        #return len(aux)
        aux = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[aux] = nums[i]
                aux += 1
        return aux