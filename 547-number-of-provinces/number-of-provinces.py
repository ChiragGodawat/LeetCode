from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connected_map = defaultdict(list)
        seen = set()
        n = len(isConnected[0])
        ans = 0

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    connected_map[i].append(j)
                    connected_map[j].append(i)
        
        def dfs(node):
            for i in connected_map[node]:
                if i not in seen:
                    seen.add(i)
                    dfs(i)
        
        for i in connected_map:
            if i not in seen:
                seen.add(i)
                dfs(i)
                ans = ans + 1
        
        return ans


        