class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(0,(len(haystack)-len(needle)+1)):
            if haystack[-1:-len(needle)]==needle:
                return len(haystack)-len(needle)
            elif haystack[i:i+len(needle)]==needle:
                return i
        return -1
        