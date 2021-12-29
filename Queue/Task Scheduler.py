class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic={}
        frequencies=[]
        task=[]
        final=[]
        for i in tasks:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in dic:
            task.append(i)
        for i in task:
            frequencies.append(dic[i])
        m=max(frequencies)
        taskswithMaxf=frequencies.count(m)
        count=max(len(tasks),(m-1)*(n+1)+taskswithMaxf)
        return count