class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            numstr = ""

            while i < len(s) and s[i] != "#":
                numstr += s[i]
                i += 1

            length = int(numstr)

            i += 1   # skip '#'

            word = ""
            for j in range(length):
                word += s[i + j]

            result.append(word)
            i = i + length

        return result