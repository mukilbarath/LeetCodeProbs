class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nl=[]
        for i in range(len(nums)):
            nl.append(nums[i])
        return nl+nums
        