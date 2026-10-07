class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "#empty"
        message = ""
        for i, word in enumerate(strs):
            for char in word:
                val = ord(char) ^ 9
                if val < 100:
                    message += "0"
                message += str(val)
            if not i == len(strs) - 1:
                s = "1!:@:#2"
                for c in s:
                    val = ord(c) ^ 9
                    if val < 100:
                        message += "0"
                    message += str(val)
        return message

    def decode(self, s: str) -> List[str]:
        if s == "#empty":
            return []
        chars = [int(s[i:i+3]) for i in range(0, len(s), 3)]
        words = "".join([chr(c ^ 9) for c in chars]).split("1!:@:#2")
        return words
