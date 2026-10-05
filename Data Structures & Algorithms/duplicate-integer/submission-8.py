class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # after testing, for some reason a map uses less 
        # memory then a set
        unique = {}
        for num in nums:
            if num in unique:
                return True
            unique[num] = 1
        return False