# class Node:
#     def __init__(self, data):
#         self.date = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return
#         else: 
#             last_node = self.head

#             while last_node.next is not None:
#                 last_node = last_node.next

#             last_node.next = new_node

#     def display(self):
#         current_node = self.head

#         while current_node is not None:
#             print(current_node.date, end="->")
#             current_node = current_node.next

# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.append(4)
# linked_list.display()


# from collections import deque

# deque_info = deque([1, 2, 3, 4, 5, 1, 5, 4])
# print(deque_info)

# print(deque_info.count(2))
# print(deque_info.count(4))

# deque_info.append(11)
# print(deque_info)

# deque_info.appendleft(22)
# print(deque_info)

# deque_info.pop()
# print(deque_info)


from queue import Queue

queue_info = Queue()
queue_info.put(1)
queue_info.put(2)
queue_info.put(3)

print(queue_info.get())
print(queue_info.get())
