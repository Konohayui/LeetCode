"""
O(log(m+n))
"""
class Solution:
    def getKth(self, nums1, nums2, k):
        len1, len2 = len(nums1), len(nums2) # assume nums1 is the shortest
        if len1 > len2:
            return self.getKth(nums2, nums1, k)
        if len1 == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        pos1 = min(k//2, len1)
        pos2 = k - pos1
        
        if nums1[pos1 - 1] < nums2[pos2 - 1]:
            return self.getKth(nums1[pos1:], nums2, pos2)
        else:
            return self.getKth(nums1, nums2[pos2:], pos1)
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, (len1 + len2)//2 + 1)
        return (self.getKth(nums1, nums2, (len1 + len2)//2) + self.getKth(nums1, nums2, (len1 + len2)//2 + 1))*0.5
    

"""
O(m+n)
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        """
        new_list = nums1 + nums2
        new_list = sort(new_list)
        
        # time complexity isn't O(log(m+n))
        """
        new_list = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new_list.append(nums1[i])
                i += 1
            else:
                new_list.append(nums2[j])
                j += 1
        
        # print(new_list)
        if i == len(nums1):
            new_list.extend(nums2[j:])
        elif j == len(nums2):
            new_list.extend(nums1[i:])
            
        if len(new_list) % 2 == 1:
            return new_list[len(new_list)//2]
        else:
            return (new_list[len(new_list)//2 - 1] + new_list[len(new_list)//2])/2
