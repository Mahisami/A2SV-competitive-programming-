class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums1)
        n1 = len(nums2)
        # min_val = 
        
        
        while l < n and r < n1:
            if nums1[l] == nums2[r]:
                return nums1[l]
            elif nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        return -1
                
            
                
                
                
        