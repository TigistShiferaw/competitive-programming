class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        if len(merged) %2 == 0:
            ind = len(merged)//2
            return (merged[ind -1] + merged[ind])/2
        index = len(merged)//2
        return merged[index]