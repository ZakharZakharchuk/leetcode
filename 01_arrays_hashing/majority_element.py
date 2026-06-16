class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        votes_count = 0
        voter = None
        for num in nums:
            if votes_count > 0:
                if num == voter:
                    votes_count += 1
                else:
                    votes_count -= 1
            else:
                voter = num
                votes_count = 1

        return voter


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(nums))
