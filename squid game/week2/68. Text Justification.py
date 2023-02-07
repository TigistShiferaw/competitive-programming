class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        ans = []
        i = 0

        while i < len(words):
            space = 0
            tmp = []
            cnt = 0
            p = 0
            while i < len(words) and space + cnt + len(words[i]) <= maxWidth:
                cnt += len(words[i])
                space += 1
                p = 1
                tmp.append(words[i])
                i += 1
            
            remain = maxWidth - cnt
            
            mod = 0
            div = 0
            if space - 1 > 0:
                div = remain // (space - 1)
                mod = remain % (space - 1)
            line  = ""
            if i <= len(words) - 1:
                for k in range(len(tmp)):
                    line += tmp[k]
                    if k < len(tmp) -1:
                        sp = " " * div
                        line += sp
                    if mod > 0:
                        line += " "
                        mod -= 1
                
            else:
                print(tmp)
                for k in range(len(tmp)):
                    line += tmp[k]
                    if k < len(tmp) - 1:
                        line += " "
            # print(line)
            while len(line) < maxWidth:
                line += " "
            while len(line) > maxWidth:
                line = line[:len(line) - 1]
            ans.append(line)
            
            if not p:
                i += 1
        return ans