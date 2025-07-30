class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dig=0
        for i in digits:
            dig*=10
            dig=dig+i
        dig+=1
        return [int(i) for i in str(dig)]    
        