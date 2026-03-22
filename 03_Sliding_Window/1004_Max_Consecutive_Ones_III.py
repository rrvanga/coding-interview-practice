"""
PROBLEM: 1004 Max Consecutive Ones III
STRATEGY: SLIDING WINDOW
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)

"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:

        longest = 0

        left = 0
        currZeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                currZeros += 1

            while currZeros > k:
                if nums[left] == 0:
                    currZeros -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest


if __name__ == "__main__":
    sol = Solution()
    nums, k = [1, 0, 1, 1, 1, 0], 1
    assert sol.longestOnes(nums, k) == 5
    print("Passed")
