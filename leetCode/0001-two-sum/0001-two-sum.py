class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_list = []
        for i, v in enumerate(nums):
            for j in range(i+1, len(nums)):
                if v + nums[j] == target:
                    my_list.append(i)
                    my_list.append(j)
        return my_list
        