from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        def print_value(node):
            nodes_str=[str(x) for x in self.unvisited]
            print('\t',node,'\t\t','\t'.join(nodes_str))
            
            

        def create():
            self.graph = {}
            self.unvisited = [float('inf')] * n
            self.visited = [-1] * n

            for time in times:
                if time[0] in self.graph:
                    self.graph[time[0]].append((time[1], time[2]))
                else:
                    self.graph[time[0]] = [(time[1], time[2])]

            self.unvisited[k - 1] = 0

        def min_node():
            min_index = -1
            min_value = float('inf')
            for i in range(n):
                if self.visited[i] == -1 and self.unvisited[i] < min_value:
                    min_value = self.unvisited[i]
                    min_index = i
            return min_index

        def complete():
            return all(x != -1 for x in self.visited)


        def maxi():
            maxv=-1
            for x in self.visited:
                if(x>maxv):
                    maxv=x
                if(x==-1):
                    return -1
            return maxv


        create()
        start = k - 1

        nodes_str=[str(x+1) for x in range(n)]
        print('\titer\t\t','\t'.join(nodes_str))
        print('----'*50)
        i=0
        print_value(start)
        while (start!=-1):
            
            if start + 1 in self.graph:
                for dest, cost in self.graph[start + 1]:
                    if self.visited[dest - 1] == -1:
                        self.unvisited[dest - 1] = min(self.unvisited[dest - 1], self.unvisited[start] + cost)
            self.visited[start] = self.unvisited[start]
            print_value(start)
            start = min_node()
            i+=1
        max_time = maxi()
        return max_time if max_time!=0 else -1
    
s=Solution()
n=int(input('enter number of nodes: '))
times=eval(input('enter in format [start,dest,cost]: '))
k=int(input('enter the starting node '))
# times=[[2,1,1],[2,3,1],[3,4,1]]
# n=4
# k=2
ans=s.networkDelayTime(times,n,k)
print('ans= ',ans)
