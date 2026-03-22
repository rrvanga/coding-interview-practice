class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store visited
        refMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in refMap:
                return [refMap[diff], i]
            refMap[n] = i
        return []

if __name__ == "__main__":
    sol = Solution()
    nums, target = [2, 7, 15, 11], 18
    result = sol.twoSum(nums, target)
    assert result == [1,3], f"Wrong {result}"
    print("passed")
