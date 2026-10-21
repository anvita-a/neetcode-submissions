class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_lst = []
        for i in strs:
            encode_lst.append(str(len(i)) + "#" + i)
        encode_str = "".join(encode_lst)
        print (encode_str)
        return encode_str
        

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        length = len(s)
        while i < length:
            number = ""
            while s[i] != "#":
                number += s[i]
                i += 1
            i += 1
            word = s[i : i+int(number)]
            i = i + int(number)
            lst.append(word)
        
        return lst


