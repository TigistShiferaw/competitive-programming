class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for i in range (n):
            index=i+1
            if index%3==0 and index%5==0:
                answer.append("FizzBuzz")
            elif  index%3==0 :
                answer.append("Fizz")
            elif index%5==0:
                answer.append("Buzz")
            else :
                answer.append(str(index))
                
        return answer        
                