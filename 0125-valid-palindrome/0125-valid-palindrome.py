class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_fil=''.join([i.lower() for i in s if i.isalnum()])
        if s_fil==s_fil[::-1]:
            return True
        else:
            return False
        