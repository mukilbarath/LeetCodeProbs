class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
            else:
            # We hit a 0, so update the max and reset
                if current_count > max_count:
                    max_count = current_count
                current_count = 0
            
    # Final check for streaks that end at the last index
        return max(max_count, current_count)
            


        