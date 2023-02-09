class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        relationMap = defaultdict(list)
        for i  in range(len(equations)):
            eq = equations[i]
            relationMap[eq[0]].append((eq[1],values[i]))
            relationMap[eq[1]].append((eq[0],1/values[i]))
        
        
        def soln(dividend, divisor,ans):
            visited = set()
            def calcVal(dividend, divisor,ans):
                if dividend == divisor:
                    return ans

                tmp = -1
                visited.add(dividend)
                for i in range(len(relationMap[dividend])):
                    rn = relationMap[dividend][i]
                    if (rn[0]) not in visited:
                        visited.add(rn[0])
                        tmp = max(tmp, calcVal(rn[0],divisor, ans * rn[1]))
                        visited.remove(rn[0])
                    # print(tmp)
                
                return  tmp
            return calcVal(dividend, divisor, ans)
        ans = []
        for q in queries:
            if q[0] not in relationMap or q[1] not in relationMap:
                ans.append(-1.00000)
            else:
                ans.append(soln(q[0],q[1],1))
        return ans