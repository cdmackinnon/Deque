import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

#DEQUE TESTS
  def test_empty_deque(self):
   self.assertEqual('[ ]', str(self.__deque))

  def test_empty_deque_length(self):
    self.assertEqual(0, len(self.__deque))

  def test_push_front_once_deque(self):
    self.__deque.push_front(1)
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_push_front_once_deque_length(self):
    self.__deque.push_front(1)
    self.assertEqual(1 , len(self.__deque))

  def test_push_back_once_deque(self):
    self.__deque.push_back(1)
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_push_back_once_deque_length(self):
    self.__deque.push_back(1)
    self.assertEqual(1 , len(self.__deque))

  def test_push_front_growth_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual('[ 2, 1 ]', str(self.__deque))

  def test_push_back_growth_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_back(2)
    self.assertEqual('[ 1, 2 ]', str(self.__deque))

  def test_push_growth_deque_length(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual(2 , len(self.__deque))

  #growth
  def test_growth_twice_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.assertEqual('[ 3, 2, 1 ]', str(self.__deque))

  def test_growth_three_time_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.__deque.push_front(4)
    self.__deque.push_front(5)
    self.assertEqual('[ 5, 4, 3, 2, 1 ]', str(self.__deque))

  #peek front
  def test_peek_front_empty_deque(self):
    self.assertEqual(self.__deque.peek_front(), None)

  def test_peek_front_empty_deque_string(self):
    self.__deque.peek_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_peek_front_one_element_deque(self):
    self.__deque.push_front(1)
    self.assertEqual(self.__deque.peek_front(), 1)

  def test_peek_front_one_element_deque_length(self):
    self.__deque.push_front(1)
    self.__deque.peek_front()
    self.assertEqual(1 , len(self.__deque))

  def test_peek_front_one_element_deque_string(self):
    self.__deque.push_front(1)
    self.__deque.peek_front()
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_peek_front_two_elements_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual(self.__deque.peek_front(), 2)

  #peek back
  def test_peek_back_empty_deque(self):
      self.assertEqual(self.__deque.peek_back(), None)    

  def test_peek_back_empty_deque_string(self):
    self.__deque.peek_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_peek_back_one_element_deque(self):
    self.__deque.push_front(1)
    self.assertEqual(self.__deque.peek_back(), 1)

  def test_peek_back_one_element_deque_string(self):
    self.__deque.push_front(1)
    self.__deque.peek_back()
    self.assertEqual('[ 1 ]',str(self.__deque))

  def test_peek_back_two_elements_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual(self.__deque.peek_back(), 1)

  #pop_front
  def test_pop_front_empty_deque(self):
    self.assertEqual(self.__deque.pop_front(), None)

  def test_pop_front_empty_deque_string(self):
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_one_item_deque(self):
    self.__deque.push_front(1)
    self.assertEqual(self.__deque.pop_front(), 1)

  def test_pop_front_one_item_deque_length(self):
    self.__deque.push_front(1)
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))

  def test_pop_front_one_item_pushed_from_back_deque(self):
    self.__deque.push_back(1)
    self.assertEqual(self.__deque.pop_front(), 1)

  def test_pop_front_one_item_deque_string(self):
    self.__deque.push_front(1)
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_two_items_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual(self.__deque.pop_front(), 2)

  def test_pop_front_two_items_deque_string(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_front()
    self.assertEqual('[ 1 ]', str(self.__deque))

  #pop_back
  def test_pop_back_empty_deque(self):
    self.assertEqual(self.__deque.pop_back(), None)

  def test_pop_back_empty_deque_string(self):
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))  

  def test_pop_back_one_item_deque(self):
    self.__deque.push_back(1)
    self.assertEqual(self.__deque.pop_back(), 1)

  def test_pop_back_one_item_pushed_from_front_deque(self):
    self.__deque.push_front(1)
    self.assertEqual(self.__deque.pop_back(), 1)

  def test_pop_back_one_item_deque_length(self):
    self.__deque.push_back(1)
    self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))

  def test_pop_back_one_item_deque_string(self):
    self.__deque.push_back(1)
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_two_items_deque(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.assertEqual(self.__deque.pop_back(), 2)

  def test_pop_back_two_items_deque_string(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.__deque.pop_back()
    self.assertEqual('[ 1 ]', str(self.__deque))


#STACK TESTS
  def test_empty_stack(self):
    self.assertEqual('[ ]', str(self.__stack))

  def test_empty_stack_length(self):
    self.assertEqual(0, len(self.__stack))

  def test_push_once_stack(self):
    self.__stack.push(1)
    self.assertEqual('[ 1 ]', str(self.__stack))

  def test_on_item_stack_length(self):
    self.__stack.push(1)
    self.assertEqual(1, len(self.__stack))

  def test_growth_stack(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.assertEqual('[ 2, 1 ]', str(self.__stack))

  def test_growth_twice_stack(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.push(3)
    self.assertEqual('[ 3, 2, 1 ]', str(self.__stack))

  def test_growth_three_times_stack(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.push(3)
    self.__stack.push(4)
    self.__stack.push(5)
    self.assertEqual('[ 5, 4, 3, 2, 1 ]', str(self.__stack))

  #peek
  def test_peek_empty_stack(self):
    self.assertEqual(self.__stack.peek(), None)

  def test_peek_empty_stack_string(self):
    self.__stack.peek()
    self.assertEqual('[ ]', str(self.__stack))

  def test_peek_one_item_stack(self):
    self.__stack.push(1)
    self.assertEqual(self.__stack.peek(), 1)

  def test_peek_one_item_stack_string(self):
    self.__stack.push(1)
    self.__stack.peek()
    self.assertEqual('[ 1 ]', str(self.__stack))

  def test_peek_two_items_stack(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.assertEqual(self.__stack.peek(), 2)

  #pop
  def test_pop_empty_stack(self):
    self.assertEqual(self.__stack.pop(), None)

  def test_pop_empty_stack_string(self):
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_one_item_stack(self):
    self.__stack.push(1)
    self.assertEqual(1, self.__stack.pop())

  def test_pop_one_item_stack_length(self):
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack))

  def test_pop_one_item_stack_string(self):
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_two_items_stack(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.assertEqual(2, self.__stack.pop())

  def test_pop_two_items_stack_string(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.pop()
    self.assertEqual('[ 1 ]', str(self.__stack))

#QUEUE TESTS
  def test_empty_queue(self):
    self.assertEqual('[ ]', str(self.__queue))

  def test_empty_queue_length(self):
    self.assertEqual(0, len(self.__queue))

  def test_enqueue_once_queue(self):
   self.__queue.enqueue(1)
   self.assertEqual('[ 1 ]', str(self.__queue))
  
  def test_growth_queue (self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual('[ 1, 2 ]', str(self.__queue))

  def test_growth_twice_queue (self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__queue))

  def test_growth_three_times_queue (self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.__queue.enqueue(4)
    self.__queue.enqueue(5)
    self.assertEqual('[ 1, 2, 3, 4, 5 ]', str(self.__queue))

  #peek
  def test_peek_empty_queue(self):
    self.assertEqual(self.__queue.peek(), None)

  def test_peek_empty_queue_string(self):
    self.__queue.peek()
    self.assertEqual('[ ]', str(self.__queue))

  def test_peek_one_item_queue(self):
    self.__queue.enqueue(1)
    self.__queue.peek()
    self.assertEqual(self.__queue.peek(),1 )

  def test_peek_one_item_queue_string(self):
    self.__queue.enqueue(1)
    self.__queue.peek()
    self.assertEqual('[ 1 ]', str(self.__queue))

  def test_peek_two_items_queue(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual(self.__queue.peek(), 1)

  #dequeue
  def test_dequeue_empty_queue(self):
    self.assertEqual(self.__queue.dequeue(), None)

  def test_dequeue_empty_queue_str(self):
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_one_item_queue(self):
    self.__queue.enqueue(1)
    self.assertEqual(self.__queue.dequeue(), 1)

  def test_dequeue_queue_length(self):
    self.__queue.enqueue(1)
    self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))

  def test_dequeue_one_item_queue_string(self):
    self.__queue.enqueue(1)
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_two_item_queue(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual(self.__queue.dequeue(), 1)

  def test_dequeue_two_item_queue_string(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.dequeue()
    self.assertEqual('[ 2 ]', str(self.__queue))


#TEST LENGTHS

if __name__ == '__main__':
  unittest.main()

