class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        s_list = list(s)
        left, right = 0, len(s) - 1
    
        while left < right:
        # Move left pointer until it points to a vowel
            while left < right and s_list[left] not in vowels:
                left += 1
        # Move right pointer until it points to a vowel
            while left < right and s_list[right] not in vowels:
                 right -= 1
        
        # Swap the vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
        
        # Move pointers forward to continue searching
            left += 1
            right -= 1
        
        return "".join(s_list)
        