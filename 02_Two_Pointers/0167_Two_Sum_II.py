"""
PROBLEM: 0167 TWO SUM II
STRATEGY: We have to solve the problem in constant space. so we use two pointers to track sum and increment or decrement
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)

"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        low = 0
        high = len(numbers) - 1

        while low < high:
            sum = numbers[low] + numbers[high]

            if sum == target:
                return [low + 1, high + 1]
            elif sum < target:
                low += 1
            else:
                high -= 1

        return [-1, -1]


if __name__ == "__main__":
    sol = Solution()
    nums, k = [2, 7, 11, 15], 9
    result = sol.twoSum(nums, k)
    assert result == [1, 2], f"{result}"
    print("Passed")
