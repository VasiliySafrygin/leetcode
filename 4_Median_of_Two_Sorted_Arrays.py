from typing import List


class Solution:
    def simple_merge(self, list1, list2):
        i, j = 0, 0
        res = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
        res += list1[i:]
        res += list2[j:] 
        # один из list1[i:] и list2[j:] будет уже пустой, поэтому добавится только нужный остаток
        return res

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.simple_merge(nums1, nums2)
        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2
        else:
            return nums[mid] / 1



s = Solution()
r = s.findMedianSortedArrays([1,3], [2])
print(r)
assert(r == 2.00000)



r = s.findMedianSortedArrays([1,3,4,5], [2, 10])
print(r)
assert(r == 3.5)
