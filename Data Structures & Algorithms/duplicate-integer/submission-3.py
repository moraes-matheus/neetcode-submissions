class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        previous = []
        for i in range(len(nums)):
            if nums[i] in previous:
                return True
            previous.append(nums[i])
        return False