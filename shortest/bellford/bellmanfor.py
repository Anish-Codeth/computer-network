from typing import List

class Solution:
    def values(self,iter):
        for i,x in enumerate(self.nodes):
            print('\t',iter,'\t''\t',i,'\t','\t',x)

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        iters=n-1
        self.nodes=[float('inf')]*n
        self.nodes[k-1]=0

        print('\tIter\t\tNodes\t\tWeight')
        for i in range(iters):
            self.values(i)
            for src,dest,cost in times:
                self.nodes[dest-1]=min(self.nodes[dest-1],self.nodes[src-1]+cost)
                
            print('-'*50)
        self.values(n-1)

        return max(self.nodes) if max(self.nodes)!=float('inf') else -1
    





s=Solution()
n=int(input('enter number of nodes: '))
times=eval(input('enter in format [start,dest,cost]: '))
k=int(input('enter the starting node '))
# times=[[2,1,1],[2,3,1],[3,4,1]]
# n=4
# k=2
ans=s.networkDelayTime(times,n,k)
print('ans= ',ans)