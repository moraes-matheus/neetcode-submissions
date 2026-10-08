class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        strs = list()
        size = ""
        i = 0
        while i < len(s):
            while s[i] != "#":
                size += s[i]
                i += 1
            i += 1
            strs.append(s[i:i+int(size)])
            i += int(size)
            size = ""
        return strs
