def Queue():
    queue=[]
    return queue
def isEmpty(q):
    return len(q)==0
def Enqueue(q,data):
    q.append(data)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)

from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.adj=[[] for i in range(self.v)]
    def addEdge(self,u,v,w):
        self.adj[u].append([v,w])

    def topological(self):
        queue=Queue()
        l=[]

        indegree=[0 for i in range(self.v)]

        for i in range(self.v):
            for j in range(len(self.adj[i])):
                v=self.adj[i][j][0]

                indegree[v]+=1

        for i in range(self.v):
            if indegree[i]==0:
                Enqueue(queue,i)

        while(Size(queue)):
            u=Dequeue(queue)
            l.append(u)

            for j in range(len(self.adj[u])):
                v=self.adj[u][j][0]
                indegree[v]-=1
                if indegree[v]==0:
                    Enqueue(queue,v)

        return l
    def maxdist(self,s):
        dist=[-9999 for i in range(self.v)]
        l=self.topological()
        print(l)

        dist[s]=0

        for i in range(len(l)):
            u=l[i]

            for j in range(len(self.adj[u])):
                v=self.adj[u][j][0]
                w=self.adj[u][j][1]

                if dist[v]<(dist[u]+w):
                    dist[v]=dist[u]+w

        print(dist)


g=Graph(6)
g.addEdge(0, 1, 5);
g.addEdge(0, 2, 3);
g.addEdge(1, 3, 6);
g.addEdge(1, 2, 2);
g.addEdge(2, 4, 4);
g.addEdge(2, 5, 2);
g.addEdge(2, 3, 7);
g.addEdge(3, 5, 1);
g.addEdge(3, 4, -1);
g.addEdge(4, 5, -2);
g.maxdist(1)
