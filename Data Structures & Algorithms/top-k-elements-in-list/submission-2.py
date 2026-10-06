class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if not num in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        values = []
        key = 0
        for i in range(k):
            greater = 0
            for k,v in frequency.items():
                if k not in values and v > greater:
                    greater = v
                    key = k
            values.append(key) 
        return values
        

        
            