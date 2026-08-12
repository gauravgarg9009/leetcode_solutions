class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        i,j,k=m-1,n-1,m+n-1
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
        elif n==0:
            return nums1
        while j>=0:
            if i>=0 and nums1[i]>=nums2[j]:
                nums1[k]=nums1[i]
                i=i-1
            else:
                nums1[k]=nums2[j]
                j=j-1
            k=k-1