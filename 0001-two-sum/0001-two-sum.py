class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        passed = {}
        answer = []
        for i, num in enumerate(nums):
            if (target - num) in passed:
                answer = [passed[(target - num)], i]
            else:
                passed[num] = i
        return answer



        



                