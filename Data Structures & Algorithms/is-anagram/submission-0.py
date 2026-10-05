class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for char in t:
            if not char in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        for k,v in char_count.items():
            if not v == 0:
                return False
        return True
        