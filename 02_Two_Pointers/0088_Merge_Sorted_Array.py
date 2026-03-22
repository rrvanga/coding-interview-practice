"""
PROBLEM: 0088 Merge Sorted Array
STRATEGY: Three pointers. Focus on iterating and figuring out what value to be added at the end.
constraints are important
TIME COMPLEXITY: O(m + n)
SPACE COMPLEXITY: O(1)

"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1

        for p in range(m + n - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1


if __name__ == "__main__":
    sol = Solution()
    nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]
    print("Passed")
