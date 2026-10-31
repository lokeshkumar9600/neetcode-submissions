class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        adjacency_list = {i:[] for i in range(n)}

        for u,v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        visited = set()


        def dfs(node):
            visited.add(node)

            for neighbours in adjacency_list[node]:
                if neighbours not in visited:
                    dfs(neighbours)

        
        dfs(0)
        return len(visited) == n

        


        