class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__top == self.__max_size - 1:
          #print('fault')
          return True
        else:
          return False
        #Remove pass and write the logic to check whether stack is full. If the stack is full, return true else return false.

    def top(self):
      return self.__top

    def size(self):
      return self.__max_size

    def push(self,data):
        if (self.is_full()):
          print('Stack is FULL.')
        else:
          self.__top += 1
          self.__elements[self.__top] = data
        #Remove pass and write the logic to push element into the stack. Element should be pushed only if the stack is not full. Otherwise, display appropriate message
                                          
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

stack1=Stack(5)
#Push all the required element.
stack1.push("Shirt1")

