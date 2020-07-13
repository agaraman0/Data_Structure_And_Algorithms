# https://leetcode.com/problems/partition-equal-subset-sum/submissions/
def canPartition(self, nums: List[int]) -> bool:
        
        tot = sum(nums)
        
        if tot%2 == 1:
            return False
        
        tot = tot//2
        def knapsack(nums,tot,i):
            
            if tot == 0:
                return True
            
            if i<0:
                return False
            
            ans = False
            
            if tot - nums[i]>=0:
                ans = knapsack(nums,tot-nums[i],i-1) or knapsack(nums,tot,i-1)
        
            return ans
        
        return knapsack(nums,tot,len(nums)-1)