"""
PROBLEM: 0125 Valid palindrome
STRATEGY: We have to start with 2 pointers on the ends and move inwards while ignoring non alpha numeric
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    result = sol.isPalindrome("A man, a plan, a canal: Panama")
    assert result, f"{result}"
    print(f"Passed: {result}")
