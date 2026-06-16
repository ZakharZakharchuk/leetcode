from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        character_map = Counter(s)
        for ch in t:
            counter = character_map.get(ch, 0)
            if counter == 0:
                return False
            character_map[ch] = counter - 1
        return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))  # expected: True

