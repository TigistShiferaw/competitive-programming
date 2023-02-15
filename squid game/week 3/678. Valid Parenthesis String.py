class Solution:
    def checkValidString(self, s: str) -> bool:
        prefixOpening = [0] * len(s)
        prefixClosing = [0] * len(s)
        suffixOpening = [0] * len(s)
        suffixClosing = [0] * len(s)
        suffixStar = [0] * len(s)
        prefixStar = [0] * len(s)
        if s[0] == "*":
            prefixStar [0] = 1
        elif s[0] == "(":
            prefixOpening[0] = 1
        else:
            prefixClosing[0] = 1
        if s[-1] == "*":
            suffixStar[-1] = 1
        
        elif s[-1] == ")":
            suffixClosing[-1] = 1
        else:
            suffixOpening[-1] = 1

        for i in range(1,len(s)):
            if s[i] == "(":
                prefixOpening[i] = prefixOpening[i -1] + 1
                prefixStar [i] = prefixStar[i - 1] 
                prefixClosing[i] = prefixClosing[i -1] 
            elif s[i] ==  "*":
                prefixStar[i] = prefixStar[i - 1] + 1
                prefixOpening[i] = prefixOpening[i - 1]
                prefixClosing[i] = prefixClosing[i -1] 
            else:
                prefixClosing[i] = prefixClosing[i -1] + 1
                prefixStar [i] = prefixStar[i - 1]
                prefixOpening[i] = prefixOpening[i - 1]

        for i in range(len(s) -2, -1, -1):
            if s[i] == ")":
                suffixClosing[i] = suffixClosing[i + 1] + 1
                suffixStar [i] = suffixStar[i + 1] 
                suffixOpening[i] = suffixOpening[i  + 1]
            elif s[i] ==  "*":
                suffixStar[i] = suffixStar[i + 1] + 1
                suffixClosing[i] = suffixClosing[i + 1]
                suffixOpening[i] = suffixOpening[i  + 1]
            else:
                suffixOpening[i] = suffixOpening[i + 1] + 1
                suffixStar [i] = suffixStar[i + 1] 
                suffixClosing[i] = suffixClosing[i + 1]
        
        for i in range(len(s)):
            if s[i] == ")" and prefixStar[i] + prefixOpening[i] < prefixClosing[i]:
                return False
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(" and suffixStar[i] + suffixClosing[i] < suffixOpening[i]:
                return False
        return True
                
