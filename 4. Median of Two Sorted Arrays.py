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
