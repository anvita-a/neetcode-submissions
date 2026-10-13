class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for i in strs:
            encode_str += str(len(i)) + "#" + i
        return encode_str

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            number = ""
            while s[i] != "#":
                if s[i].isdigit():
                    number += s[i]
                    i += 1
            i += 1
            word = ""
            for j in range(i, i + int(number)):
                word += s[j]
                i += 1
            lst.append(word)
        return lst


