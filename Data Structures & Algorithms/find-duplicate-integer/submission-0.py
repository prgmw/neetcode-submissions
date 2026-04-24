class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        has_item = set()
        
        for item in nums:
            if item in has_item:
                return item
            else:
                has_item.add(item)
        
        return 0
        