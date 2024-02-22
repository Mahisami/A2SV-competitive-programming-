class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = []
        
        for i in nums1:
            out = -1
            ind = nums2.index(i) + 1
            
            while ind < len(nums2):
                if i < nums2[ind]:
                    out = nums2[ind]
                    break
                ind += 1
            x.append(out)
        return x

                    
            
        