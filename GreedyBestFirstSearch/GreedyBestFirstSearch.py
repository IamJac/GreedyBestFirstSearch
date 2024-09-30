import heapq
def gbfs(graph,heuristics,goal,start):
    pq=[]
    visited=set()
    heapq.heappush(pq,(heuristics[start],start))
    num=0
    while pq:
        _, node=heapq.heappop(pq)
        if node==goal:
            print(F"{goal} has been found in {num} steps")
            return
        if node not in visited:
            visited.add(node)
            for i,cost in graph.get(node,[]):
                if i not in visited:
                    heapq.heappush(pq,(heuristics[i],i))
                    num+=1
    print(F"{goal} not found")

def get_heuristics():
    data={'A':6,'B':4,'C':2,'D':5,'E':8,'F':7,'G':5,'H':1,'I':0 }
    return data
graph = {
    'A': [('B', 1), ('C', 1), ('F', 1), ('G', 1)],
    'B': [('A', 1), ('C', 1), ('D', 1), ('G', 1)],
    'C': [('A', 1), ('B', 1), ('D', 1), ('E', 1), ('F', 1), ('G', 1)],
    'D': [('B', 1), ('C', 1), ('E', 1), ('F', 1)],
    'E': [('C', 1), ('D', 1), ('F', 1)],
    'F': [('A', 1), ('C', 1), ('D', 1), ('E', 1), ('G', 1), ('H', 1)],
    'G': [('A', 1), ('B', 1), ('C', 1), ('F', 1)],
    'H': [('F', 1), ('I', 1)],
    'I': [('H', 1)]
        }
heuristics=get_heuristics()
gbfs(graph,heuristics,'I','A')