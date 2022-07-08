from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    #capacity starts at 1; we will grow on demand.
    #front and back are None when the Deque is empty
    #After the deque is filled and emptied it returns to this front and back state
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__front = None  
    self.__back = None
    self.__size = 0


  def __str__(self):
    #String oriented from front (left) to back (right).
    output = '['

    for i in range(self.__size):
      index = self.__front - i
      #this if statement allows for a circular array when the index is decreasing
      if index < 0:
        index += self.__capacity
      output = output + ' ' + str(self.__contents[index])
      if (self.__size > 1 and i < self.__size - 1):
           output = output + ','
    return output + ' ]'
    

  def __len__(self):
    return self.__size


  def __grow(self):
    #This doubles the array size
    #Old array values are inserted starting at index 0; this helps maintain structure
    old_capacity = self.__capacity
    self.__capacity *= 2
    new_contents = [None] * self.__capacity

    #the front and back markers can end up on different sides of each other, this checks that
    newIndex = 0
    if self.__back < self.__front:
      for i in range(self.__back, self.__front+1):
        new_contents[newIndex] = self.__contents[i%(old_capacity+1)] 
        newIndex +=1
    else:
      for i in range(self.__size):
        new_contents[newIndex] = self.__contents[(self.__back+i)%(old_capacity)]  
        newIndex +=1
    
    self.__front = self.__size-1
    self.__back = 0
    self.__contents = new_contents
    


  def push_front(self, val):
    if self.__size == self.__capacity:
      self.__grow()
  
    if self.__front is None:
      self.__front = 0
    else: 
      self.__front = (self.__front+1)%(self.__capacity) #capacity already +1 with respect to indexing 
    self.__contents[self.__front] = val

    if self.__back is None:
      self.__back = 0

    self.__size += 1
    


  def pop_front(self):

    if self.__size == 0:
      return 

    val = self.__contents[self.__front]
    self.__front -= 1
    if self.__front < 0:
      self.__front += self.__capacity

    self.__size -= 1

    #if the set is empty this returns it to its original None State
    if self.__size == 0:
      self.__front = None
      self.__back = None

    return (val)
    
  def peek_front(self):
    if self.__size == 0:
      return

    return(self.__contents[self.__front])
    
  def push_back(self, val):
    if self.__size == self.__capacity:
      self.__grow()

    if self.__back is None:
        self.__back = 0
    else:
      self.__back -= 1
      if self.__back < 0:
        self.__back += self.__capacity
    self.__contents[self.__back] = val

    if self.__front is None:
        self.__front = 0

    self.__size += 1


  def pop_back(self):        
    if self.__size == 0:
      return

    val = self.__contents[self.__back]
    self.__back += 1
    if self.__back >= self.__capacity:
      self.__back -= self.__capacity

    self.__size -= 1
    
    if self.__size == 0:
      self.__front = None
      self.__back = None
    return (val)

  def peek_back(self):
    if self.__size == 0:
      return

    return(self.__contents[self.__back])

# No main section is necessary. Unit tests take its place.
if __name__ == '__main__':
   pass

 #Note that no exceptions are raised by any methods in Deque, Stack, or Queue.