class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rlist=[]
        for i in range(0,len(nums)):
            flag=False
            for j in range(i+1,len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        rlist.append(i)
                        rlist.append(j)
                        break
                else:
                    continue
        
        return rlist

        