#adding elemnets to the queue

class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
        
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if self.__rear == self.__max_size - 1:
          return True
        else:
          return False
        
    
    def enqueue(self,data):
        if self.is_full():
          print("Queue is FULL!")
        else:
          self.__rear += 1
          self.__elements[self.__rear] = data
    
    def display(self):
        while(self.__front <= self.__rear):
          print(self.__elements[self.__front])
          self.__front += 1
        self.__front = 0
                                                  
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg



queue1=Queue(5)
#Enqueue all the required element(s).
queue1.enqueue("Tom")
queue1.enqueue("Sam")
#Display all the elements in the queue.
queue1.display()
                                              
