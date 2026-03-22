"""
PROBLEM: 0643_Maximum Average Subarray I
STRATEGY: SLIDING WINDOW
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)

"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr = 0

        for i in range(k):
            curr = curr + nums[i]

        maxSum = curr

        for i in range(k, len(nums)):
            curr = curr + nums[i] - nums[i - k]

            maxSum = max(maxSum, curr)

        return maxSum / k


if __name__ == "__main__":
    sol = Solution()
    nums, k = [1, 3, 2, 7, 4], 2
    result = sol.findMaxAverage(nums, k)
    assert result == 5.5, f"{result}"
    print("Passed")
