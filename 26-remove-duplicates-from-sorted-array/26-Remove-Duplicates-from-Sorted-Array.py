class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """ 
        [1,3,4,3,4,4,5,5,7].  i=0,1,2, j=1,2,3,
        """
        i=0
        j=i+1

        while j< len(nums):
            if nums[j]!=nums[i]:
                i+=1
                nums[j],nums[i]=nums[i],nums[j]
            j+=1

        return len(nums[:i+1])

    
            

            
        