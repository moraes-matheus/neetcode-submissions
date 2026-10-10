class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for num in nums]
        for i in range(len(nums) - 1):
            output[i + 1] = output[i] * nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, 0, -1):
            output[i] *= postfix
            postfix *= nums[i]
        output[0] *= postfix
        
        return output
                