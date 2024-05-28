def enqueue (Q,ele):
    Q. append(ele)
    print(Q, "inserted into queue successfully ")

def dequeue():
    if len(Q)== 0:
        print("queue is empty")
        return 
    print (Q[0], " deleted successfully ") 
    Q.pop(0)


Q = []
enqueue(Q, 21)
enqueue(Q, 22)
enqueue(Q, 23)
enqueue(Q, 24)
print(Q)

dequeue(Q)
dequeue(Q)
dequeue(Q)
dequeue(Q)
print(Q)
              
              
              
              
              
              
              
              
              
     
              

    