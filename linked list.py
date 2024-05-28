class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printlinkedList(head):
    currentNode = head
    while curentNode ! =None:
       print(currentNode,data,end ="-->")
       currentNode = currentNode.next
    print()

def insertAtTail(head,ele):
    temp = Node(ele)
    if head ==None:
       return temp

    tail = head
    while tail.next != None:
          tail = tail.next
    tail.next = temp
    return head

#Task - 1
def insetAtHead(head,ele):
    temp = Node(ele)
    temp.next = head
    return temp

#Task - 2
def insertAtSpecificPosition(head,possition,ele):
    if position == 0:
        return insertAtHead(head,ele)
    
    temp = Node(ele)
    index = 0
    currentNode = head

    while index ! = postion -1:
        currentNode = currentNode.next
        index += 1

    nextNode = currentNode.next
    temp.next = temp
    return head






     

