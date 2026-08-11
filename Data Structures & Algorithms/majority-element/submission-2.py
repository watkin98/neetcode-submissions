class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            
            if count[num] > majority:
                return num
        
        return -1