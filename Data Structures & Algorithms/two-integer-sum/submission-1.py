class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in hashtable:
                return list([hashtable[value], i])
            hashtable[nums[i]] = i