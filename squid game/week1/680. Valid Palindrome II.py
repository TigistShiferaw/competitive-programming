class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalendrome(string):
            i = 0
            j = len(string) - 1
            while i <= j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True

        
        misMatched = []
       
        i = 0
        j = len(s) - 1
        while i <= j:
            
            if s[i] != s[j]:
                misMatched = [i,j]
                break
            i += 1
            j -= 1
        noDel = s
        leftDel = s[:i] + s[i + 1:]
        rightDel = s[:j] + s[j + 1:]

        return isPalendrome(noDel) or isPalendrome(leftDel) or isPalendrome(rightDel)
