class Solution:
    def sortSentence(self, s: str) -> str:
            wordsArray=s.split()
            sortedOne=" "
            for j in  range(len(wordsArray)):
                for i in range(len(wordsArray)):
            
                     word1=wordsArray[j]
                     word2=wordsArray[i]
                     if int(word1[-1]) < int(word2[-1]):
                        wordsArray[i],wordsArray[j]=wordsArray[j],wordsArray[i]
            for i in range(len(wordsArray)):
                wordsArray[i]=(wordsArray[i])[:-1]
    
                
            return (sortedOne.join(wordsArray))