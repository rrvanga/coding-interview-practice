class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        n = len(nums)
        right = n - 1

        output = [0] * n

        for i in range(n - 1, -1, -1):
            if abs(nums[right]) > abs(nums[left]):
                output[i] = nums[right] * nums[right]
                right -= 1
            else:
                output[i] = nums[left] * nums[left]
                left += 1

        return output


if __name__ == "__main__":
    sol = Solution()
    nums = [-4, 3, -6, 7]
    assert sol.sortedSquares(nums) == [9, 16, 36, 49]
    print("passed")
