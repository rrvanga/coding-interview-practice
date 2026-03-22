class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1


if __name__ == "__main__":
    sol = Solution()
    s = ["h", "e", "l", "l", "o"]
    print(f"input {s}")
    sol.reverseString(s)
    assert s == ["o", "l", "l", "e", "h"], f"failed {s}"
    print(f"passed {s}")
