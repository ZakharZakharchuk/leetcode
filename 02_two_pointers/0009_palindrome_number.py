class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False

        string_array = str(x)

        length = len(string_array)

        for i, value in enumerate(string_array):
            if value != string_array[length-i-1]:
                return False

        return True


        