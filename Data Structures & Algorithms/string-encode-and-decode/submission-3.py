class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = []
        for i in strs:
            encode_str.append(str(len(i)) + "#" + i)
        return "".join(encode_str)
        

    def decode(self, s: str) -> List[str]:
        decode_str = []
        i = 0
        while i < len(s):
            length = []
            while s[i] != "#":
                length.append(s[i])
                i += 1
            i += 1
            number = int("".join(length))
            word = s[i:i+number]
            decode_str.append(word)
            i += number

        return decode_str
            


        

