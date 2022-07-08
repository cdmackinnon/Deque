import sys # for sys.argv, the command-line arguments
from Stack import Stack 

def delimiter_check(filename):
  delimiters = Stack()
  with open(filename) as document:
    while True:
      character = document.read(1)
      #reads in each character one at a time
      if character in '([{':
        delimiters.push(character)

      if character in ')]}':
        if character == ')' and delimiters.peek() == '(':
          delimiters.pop()
        elif character == ')' and delimiters.peek() != '(':
          return False

        if character == ']' and delimiters.peek() == '[':
          delimiters.pop()
        elif character == ']' and delimiters.peek() != '[':
          return False

        if character == '}' and delimiters.peek() == '{':
          delimiters.pop()
        elif character == '}' and delimiters.peek() != '{':
          return False


      if not character:
        return True
    

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


