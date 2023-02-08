class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a in adjacentPairs:
            graph[a[0]].add(a[1])
            graph[a[1]].add(a[0])
        
        ans = []
        def dfs(i):
            if not graph[i]:
                ans.append(i)
                return
            x = graph[i].pop()
            ans.append(i)
            graph[x].remove(i)
            dfs(x)
            return
        start = inf
        for g in graph:
            if len(graph[g]) == 1:
                start = g
                break
        dfs(start)
        return ans