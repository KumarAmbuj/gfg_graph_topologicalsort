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

class Graph:
    def __init__(self,v):
        self.v=v
        self.adj=[[]for i in range(self.v)]
    def addEdge(self,u,v,w):
        self.adj[u].append([v,w])

    def topological(self):
        queue=Queue()
        l=[]
        indegree=[ 0 for i in range(self.v)]

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
    def findmax(self):

        l=self.topological()
        mx=0

        for i in range(len(l)):
            dist=[-999 for k in range(self.v)]

            dist[l[i]]=0

            for j in range(len(l)):

                u=l[j]

                for m in range(len(self.adj[u])):
                    v=self.adj[u][m][0]
                    w=self.adj[u][m][1]

                    if dist[v]<dist[u]+w:
                        dist[v]=dist[u]+w

            mx=max(mx,max(dist))

        print(mx)
g=Graph(7)
g.addEdge(1,2,3)
g.addEdge(2,3,4)
g.addEdge(2,6,2)
g.addEdge(6,4,6)
g.addEdge(6,5,5)

g.findmax()







