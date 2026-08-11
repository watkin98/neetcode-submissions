class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        count = 0
        start = 0

        while count < n:
            prev = nums[start]
            current = start
            while True:
                next_index = (current + k) % n
                nums[next_index], prev = prev, nums[next_index]
                count += 1
                current = next_index

                if current == start:
                    break
            start += 1
            