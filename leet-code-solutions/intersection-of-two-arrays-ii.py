class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new_array = []
        for i in nums1:
            if i in nums2:
                new_array.append(i)
                nums2.remove(i)
        return new_array