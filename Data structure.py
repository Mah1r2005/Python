#Stack
"""
A stack is a simple data structure that adds and removes elements in a particular order.
Every time an element is added,
it goes on the "top" of the stack.
Only an element at the top of the stack can be removed
, just like a stack of plates. This behavior is called LIFO (Last In, First Out).
Terminology
Adding a new element onto the stack is called push.
Removing an element from the stack is called pop.

Applications
Stacks can be used to create undo-redo functionalities, parsing expressions (infix to postfix/prefix conversion), and much more.
"""

class stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)
        
st=stack()
st.push(4)
print(st.items)
st.push(5)
st.print_stack()
st.pop()
print(st.items)

"""
As you can see, it's easy to create a stack using a list.
We use a list called items to store our elements.
The push method adds an element at the beginning of the list, while the pop method removes the first element of the list.
"""
#Queue
"""

A queue is similar to a stack, but defines a different way to add and remover elements.
The elements are inserted from one end, called the rear, and deleted from the other end, called the front.
This behavior is called FIFO (First in First Out).

Terminology\

The process of adding new elements into the queue is called enqueue.
The process of removal of an element from the queue is called dequeue.

Applications
Queues are used whenever we need to manage objects in order starting with the first one in.
Scenarios include printing documents on a printer, call center systems answering people on hold, and so on. 
"""


class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop(0)

    def print_queue(self):
        print(self.items)
        
st=Queue()
st.enqueue(4)
print(st.items)
st.enqueue(5)
st.print_queue()
st.dequeue()
print(st.items)
"""
The enqueue method adds an element at the beginning of the list, while the dequeue method removes the last element. 
"""
#Linked list
"""

A linked list is a sequence of nodes where each node stores its own data and a link to the next node.
One node links to another forming what can be thought of as a linked chain:
The first node is called the head,
and it's used as the starting point for any iteration through the list.
The last node must have its link pointing to None to determine the end of the list.

Unlike stacks and queues, you can insert and remove nodes in any position of the linked list (similar to a standard list).

Applications


Linked lists are useful when your data is linked.
For example when you need undo/redo functionality,
the nodes can represent the state with links to the previous and next states.
Another example would be a playlist of music, where each clip is linked with the next one.
"""
class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next


class LinkedList:
    def __init__(self):
        self.head=None

    def add_at_front(self,data):
        self.head=Node(data,self.head)

    def add_at_end(self,data):
        if not self.head:
            self.head=Node(data,None)
            return
        curr=self.head
        while curr.next:
            curr.next=Node(data,None)

    def get_last_node(self):
        n=self.head
        while(n.next!=None):
            n=n.next
        return n.data

    def print_list(self):
        n=self.head
        while n!=None:
            print(n.data,end="=>")
            n=n.next
        print()

ll=LinkedList()
ll.add_at_front(3)
ll.add_at_end(5)
ll.get_last_node()
ll.print_list()
"""
The add_at_front() method adds a new Node as the head of the list and links the previous head to it.
The add_at_end() method iterates to the end of the list using a while loop and adds the new node as the link of the last node.
"""
#Graph
"""
Graphs are used to represent many real-life applications like networks,
transportation paths of a city, and social network connections.

A graph is a set of connected nodes where each node is called a Vertex and the connection between two of them is called an Edge.
This can represent, for example, connections on a social network, where each Vertex represents a person and the Edges represent connections. 

0 1 1

1 0 0

1 0 0

A graph can be represented using a square matrix, where each element represents the edges:
0 indicates no edge, while 1 indicates an edge. The rows and columns represent the vertices.

"""
class Graph():
 def __init__(self,size):
     self.adj=[[0]*size for i in range(size)]
     self.size=size

 def add_edge(self,orig,dest):
     if orig > self.size or dest >self.size or orig <0:
         print("Invalid Edge")
         
     else:
         self.adj[orig-1][dest-1]=1
         self.adj[dest-1][orig-1]=1

 def remove_edge(self,orig,dest):
     if orig > self.size or dest > self.size or orig < 0 or dest <0:
         print("Invalid Edge")
     else:
        self.adj[orig-1][dest-1]=0
        self.adj[dest-1][orig-1]=0
    
 def display(self):
     for row in self.adj:
         print()
         for val in row:
             print('{:4}'.format(val),end="")


gr=Graph(3)
gr.display()
print()
gr.add_edge(1,0)
gr.display()

"""
We store the matrix in a two-dimensional list, called adj.
The __init__ method creates the adj matrix with the given size (number of vertices) and initializes all values to zeros.
The add_edge() method is used to add an edge by setting the corresponding values to 1.
Similarly, the remove_edge() method sets the values to 0.
"""












    
