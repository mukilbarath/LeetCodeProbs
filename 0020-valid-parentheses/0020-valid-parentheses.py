class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the topmost element from the stack if it's not empty
                # Otherwise, assign a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # The mapping for the closing bracket must match the popped element
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, we have a valid string
        return not stack
        