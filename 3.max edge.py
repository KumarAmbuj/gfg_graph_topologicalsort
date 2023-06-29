def Queue():
    queue=[]
    return queue
def isEmpty(q):
    return len(q)==0
def Enqueue(q,data):
    q.append(data)
def Dequeue(q):
    return q.pop(0)
def size(q):
    return len(q)

from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topological(self):
        queue=Queue()
        l=[]

        indegree=[0 for i in range(self.v)]

        for x in self.graph:
            for v in self.graph[x]:
                indegree[v]+=1
        for i in range(self.v):
            if indegree[i]==0:
                Enqueue(queue,i)

        while(size(queue)):

            u=Dequeue(queue)

            l.append(u)

            for i in self.graph[u]:
                indegree[i]-=1
                if indegree[i]==0:
                    Enqueue(queue,i)

        return l


    def maxedge(self):
        l=self.topological()

        for i in range(len(l)-1):
            visited=[False for i in range(self.v)]

            for v in self.graph[l[i]]:
                visited[v]=True

            for j in range(i+1,len(l)):
                if visited[l[j]]==False:
                    print(l[i],'-',l[j],end=' ')

g=Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print(g.maxedge())