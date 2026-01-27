class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num: # Faster than 'if num == 1'
                current_count += 1
            else:
                if current_count > max_count:
                    max_count = current_count
                current_count = 0
        
        # Final comparison for streaks ending at the last element
        return max_count if max_count > current_count else current_count
            


        