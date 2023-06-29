def Queue():
    queue=[]
    return queue
def isEmpty(queue):
    return len(queue)==0
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)

from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)


    def topological(self):
        visited=[False for i in range(self.v)]
        l=[]
        queue=Queue()

        indegree=[0 for i in range(self.v)]

        for x in self.graph:
            for i in self.graph[x]:
                indegree[i]+=1

        for i in range(self.v):
            if indegree[i]==0:
                Enqueue(queue,i)
        count=0

        while(Size(queue)):
            u=Dequeue(queue)

            l.append(u)

            for i in self.graph[u]:
                indegree[i]-=1
                if indegree[i]==0:
                    Enqueue(queue,i)
            count+=1

        if count==self.v:
            print(l)
        else:
            print('no possible')

g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1); 
g.addEdge(2, 3);
g.addEdge(3, 1);
g.topological()






