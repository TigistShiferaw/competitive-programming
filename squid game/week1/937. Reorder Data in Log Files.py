class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = defaultdict(str)
        letter = defaultdict(str)
        cnt = 0
        dic = defaultdict(list)
        for i in range(len(logs)):
            words = []
            j = 0
            isLetter = False
            while j < len(logs[i]):
                temp = ""
                while j < len(logs[i]) and logs[i][j] != " ":
                    temp += logs[i][j]
                    j += 1
                words.append(temp)
                j += 1
            # print(words)
            string = ""
            
            for i in range(1, len(words)):
                # print(words[i])
                if not words[i].isdigit():
                    isLetter = True
                string += words[i]
                if i < len(words) - 1:
                    string += " "
            if isLetter:
                dic[string].append(words[0])
                letter[(cnt, words[0])] = string
            else:
                digit[(cnt, words[0])] = (cnt, string)
            cnt += 1

        letters = sorted(letter.items(), key = lambda x:x[1])
        digits = sorted(digit.items(), key = lambda x:x[1])
        for d in dic:
            dic[d].sort(reverse = True)
        ans = []
        i = 0
        
        while i < len(letters):
            
            while i < len(letters) and len(dic[letters[i][1]]) >= 1:
                temp = dic[letters[i][1]].pop() + " " + letters[i][1]
                ans.append(temp)
                i += 1
            else:
                if i < len(letters):
                    temp = letters[i][0][1] + " " + letters[i][1]
                    ans.append(temp)
                    i += 1
                
        # for i in range(len(letters)):
            
            
        for i in range(len(digits)):
            temp = digits[i][0][1] + " " + digits[i][1][1]
            ans.append(temp)
        return ans