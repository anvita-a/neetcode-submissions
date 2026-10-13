class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = []
        for i in strs:
            encode_str.append(str(len(i)) + "#" + i)
        return "".join(encode_str)

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            number = ""
            while s[i] != "#":
                number += s[i]
                i += 1
            i += 1
            word = s[i : i + int(number)]
            i += int(number)
            lst.append(word)
        return lst


