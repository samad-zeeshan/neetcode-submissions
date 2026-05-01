from typing import List, Dict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        
        distance = [float("inf")] * n
        distance[src] = 0
        
        heap = [(0, src)] 
        
        while heap:
            d, u = heapq.heappop(heap)
            
            if d > distance[u]:
                continue
            
            for v, w in adj[u]:
                new_dist = d + w
                if new_dist < distance[v]:
                    distance[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))
        1
        return {i: (distance[i] if distance[i] != float("inf") else -1) for i in range(n)}



