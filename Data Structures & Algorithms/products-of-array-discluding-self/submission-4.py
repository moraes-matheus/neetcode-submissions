class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
        
        if zeros > 1:
            return [0 for num in nums]
        
        product = 1
        for num in nums:
            if num != 0:
                product *= num
        
        if zeros == 1:
            return [0 if num!=0 else product for num in nums]

        return [product // num for num in nums] 
                