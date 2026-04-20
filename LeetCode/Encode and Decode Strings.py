class Solution:
    def encode(self, strs: List[str]) -> str:
        chars = []
        for word in strs:
            chars.append(f"{len(word)}#{word}")
        return "".join(chars)
    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i in range(len(s)):
            leng = ""
            for j in range(i, len(s)):
                if s[j] == "#":
                    leng = int(leng)
                    print(j+ 1, j + leng + 1)
                    output.append(s[j+ 1: leng +j + 1])
                    i = j + leng + 1
                    break
                leng += s[j]
        return output

# Time Complexity = O(n) where n is the total length of all strings in strs
# Space Complexity = O(n) where n is the total length of all strings in strs