import re


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    solver = Solution()

    s = "anagram"
    t = "nagaram"

    result = solver.isAnagram(s,t)
    print(result)
