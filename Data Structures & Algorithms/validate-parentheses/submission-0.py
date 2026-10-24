class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = {')':'(', '}':'{', ']':'['}
        lst = []
        for i in range(len(s)):
            lst.append(s[i])
            if len(lst) >= 2:
                if s[i] in paren_dict:
                    if lst[-2] == paren_dict[s[i]] :
                        lst.pop()
                        lst.pop()

            
        return (lst == [])

        