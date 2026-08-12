class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left=0
        max_sum=float('-inf')
        sum=0


        for right in range(len(nums)):
            sum+=nums[right]
            if sum<0:
                max_sum=max(max_sum,sum)
                sum=0
            else:
                max_sum=max(max_sum,sum)

        return max_sum

        
        