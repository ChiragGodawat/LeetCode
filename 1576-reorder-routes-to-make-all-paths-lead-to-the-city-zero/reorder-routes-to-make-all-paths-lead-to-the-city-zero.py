from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connection_map = defaultdict(list)
        seen = set()
        roads = set()

        for array in connections:
            i = array[0]
            j = array[1]

            connection_map[i].append(j)
            connection_map[j].append(i)

            roads.add((i,j))
        
        ans = 0

        def dfs(node):
            nonlocal ans
            for i in connection_map[node]:
                if i not in seen:
                    if (node, i) in roads:
                        ans = ans + 1
                    seen.add(i)
                    dfs(i)
        
        seen = {0}
        dfs(0)

        return ans


        