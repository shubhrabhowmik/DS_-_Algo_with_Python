# add to end - O(1)
# add to front - O(1)
# remove from end - O(n)
# remove from front - O(1)
# add anywhere between - O(n)
# remove anywhre between - O(n)

# append - O(1)
# pop - O(n)
# prepend - O(1)
# pop first - O(1)
# insert - O(n)
# remove - O(n)
# lookup by index - O(n)
# lookup by value - O(n)

head = {
    "value":11,
    "next": {
        "value":3,
        "next": {
            "value":23,
            "next": {
                "value":7,
                "next": None
            }
        }
    }
}

print(head['next']['next']['value'])
print("    ")
# for linked list
# print(my_linked_list.head.next.next.value)

# class LinkedList:
#     def __init__(self, value):
#         create new Node

#     def append(self, value):
#         create new Node
#         add node to end

#     def pop(self):

#     def prepend(self, value):
#         create new node
#         add node to beginning

#     def insert(self, index, value):
#         create new node
#         insert node 

#     def remove(self, index):


# LinkedList Constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Print List (printing all the items in the Linked List)
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Append in Linked List
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

    # Pop
    def pop(self):
        if self.length == 0:  # when the Linked List is empty
            return None
        temp = self.head      # when linked list not empty
        pre = self.head
        while(temp.next):     
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1      
        if self.length == 0: # when their was only one item in linked list
            self.head = None
            self.tail = None
        return temp
        #return temp.value

    # Prepend (adding node in the front)
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True  

    # Pop-first item
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp

    # Get
    def get(self, index):
        if index<0 or index>= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp =  temp.next
        return temp

    # Set
    def set_value(self, index, value):
        temp = self.get(index)  #calling method inside other method
        if temp:
            temp.value = value
            return True
        return False
        # if index<0 or index>=self.length:
        #     return None
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next
        #     temp = value
    
    # Insert
    def insert(self, index, value):
        if index < 0 or index > self.length:  
            return False   #for out of range
        if index == 0:
            return self.prepend(value)  #inserting to front
        if index == self.length:
            return self.append(value)  #inserting to end
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

        
    # Remove
    def remove(self, index):
        if index<0 or index>= self.length:
            return None
        if index  == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
        
    # Reverse a LinkedList (very important)
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

         

 my_linked_list = LinkedList(1)
 my_linked_list.append(2)
 my_linked_list.print_list()
 print("---------")

 # (2) items - returns 2 node
 print(my_linked_list.pop())
 # (1) item - returns 1 node
 print(my_linked_list.pop())
 # (0) item - return None
 print(my_linked_list.pop())
 print("-------")

 my_linked_list = LinkedList(2)
 my_linked_list.append(3)
 my_linked_list.prepend(1)
 my_linked_list.print_list()

 # For Get method
 my_linked_list = LinkedList(0)
 my_linked_list.append(1)
 my_linked_list.append(2)
 my_linked_list.append(3)

 print(my_linked_list.get(2))

# For Set_value method
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
my_linked_list.insert(1,1)
my_linked_list.set_value(1,4)
my_linked_list.print_list()
print("-------")

print(my_linked_list.remove(2), '\n')
my_linked_list.print_list()

# for reverse
my_linked_list.reverse()
print(my_linked_list.print_list())

