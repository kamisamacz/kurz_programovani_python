
from stack3_12 import LimitedStack
from quee3_12 import Queue


"""
s = Stack()

print(s)
s.push(1)
s.push(2)
s.push(3)
print(s.is_empty())

print(s)
print(s.top())

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.is_empty())
"""

"""
s = LimitedStack(2)
"""
"""
print(s)
print(s.push(1))
print(s.push(2))
print(s.push(3))

print(s.is_empty())

print(s)
print(s.top())

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.is_empty())
"""

# Příklad použití
queue = Queue()
queue.add_last(10)
queue.add_last(20)
queue.add_last(30)
queue.add_last(40)
queue.add_last(30)

print(queue.get_peek())  # Výstup: 10
print(queue.delete_first())  # Výstup: 10
print(queue.get_peek())  # Výstup: 20
print(queue.size())  # Výstup: 2
