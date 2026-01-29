class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ele_rep=set()
        for i in nums:
            if i not in ele_rep:
                ele_rep.add(i)
            else:
                return True
        return False
        

        