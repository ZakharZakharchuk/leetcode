class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest = 0
        current = 0
        for diff in gain:
            current += diff
            highest = max(highest, current)
        return highest
