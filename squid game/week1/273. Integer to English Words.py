class Solution:
    def numberToWords(self, num: int) -> str:
        Map = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen", 19:"Nineteen",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty", 90:"Ninety", 100:"Hundred",1000:"Thousand",1000000:"Million",1000000000:"Billion"}
        if num == 0:
            return "Zero"
        
        numStr = (str(num))
        # if num in Map:
        #     return Map[int(numStr[0])] + " " + Map[num]
       
        ans = []
        def name(number,c):
            nonlocal ans
            temp = str(int(number))
            tmpArr = []
            if temp != "0":
                if len(temp) <= 2:
                    if int(temp) in Map:
                        tmpArr.append(Map[int(temp)])
                    else:
                        cn = 0
                        for i in range(len(temp) - 1, -1,-1):
                            if int(temp[i]) != 0:
                                tmpArr.append(Map[int(temp[i]) * (10 ** cn)])
                            cn += 1
                else:
                    cnt = 0
                    for i in range(len(temp) - 1, -1,-1):
                        if cnt == 2:
                            if 11 <= int(temp[1:] ) <= 19:
                                tmpArr.pop()
                                tmpArr.pop()
                                tmpArr.append(Map[int(temp[1:])])
                            tmpArr.append(Map[100])

                            if tmp[i] != "0":
                                tmpArr.append(Map[int(temp[i])])
                        else:
                            if tmp[i] != "0":
                                tmpArr.append(Map[int(temp[i]) * (10**cnt)])
                        cnt += 1
                    
                        
                
                if c > 0:
                    ans.append(Map[10 ** c])
                ans +=  tmpArr

        
        i = len(numStr)
        cnt = 0
        while i > 0:
            minIndex = max(0,i - 3)
            tmp = numStr[minIndex: i]
            name(tmp,cnt)
            cnt += 3
            i -= 3
        ans.reverse()
        return " ".join(ans)