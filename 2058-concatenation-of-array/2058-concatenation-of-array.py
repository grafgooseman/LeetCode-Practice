class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2

        for i in range(len(ans)):
            # % operators could be sick sometimes
            ans[i] = nums[i % len(nums)]

        return ans