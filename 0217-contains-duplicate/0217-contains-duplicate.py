class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ele_rep=set()
        for i in nums:
            if i in ele_rep:
                return True
            ele_rep.add(i)
        return False
        

        