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

    def topologicalsort(self):

        l=[]
        queue=Queue()

        indegree=[0]*self.v

        for i in range(self.v):
            for v in self.graph[i]:
                indegree[v]+=1

        count=0

        for i in range(self.v):
            if indegree[i]==0:
                Enqueue(queue,i)

        while(size(queue)):

            u=Dequeue(queue)
            l.append(u)

            for v in self.graph[u]:
                indegree[v]-=1

                if indegree[v]==0:
                    Enqueue(queue,v)
            count+=1

        if count!=self.v:
            print('cycle found')
        else:
            print(l)


g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print("Following is a Topological Sort of the given graph")
g.topologicalsort()





