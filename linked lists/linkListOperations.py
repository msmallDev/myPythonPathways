from takeInput import Node, take_input, print_LL

head = take_input()

print_LL(head)

def insert_at_head(head, data):
    newNode = Node(data)
    newNode.next = head
    head = newNode
    return head

def insert_at_tail(head, data):
    newNode = Node(data)
    if(head is None):
        return newNode
    
    temp = head
    while(temp.next != None):
        temp = temp.next

    temp.next = newNode

    return head

# def insert_at_tail_recursively(head, data):
#     if(head is None):
#         newNode = Node(data)
#         return newNode
#     if(head.next == None):
#         newNode = Node(data)
#         head.next = newNode

#     head.next = insert_at_tail_recursively(head.next, data)

#     return head


def insert_at_index(head, data, index):
    if (index == 0):
        return insert_at_head(head, data)
    
    newNode = Node(data)
    temp = head
    count = 0

    while temp is not None and count < index - 1:
        temp = temp.next
        count += 1

    if(temp is None):
        print("Index out of bounds!")
        return head

    newNode.next = temp.next
    temp.next = newNode
    return head


def delete_at_head(head):
    if(head is None):
        return None
    
    newHead = head.next
    return newHead

def is_tail_node(node):
    if(node == None):
        return True
    if(node.next == None):
        return True
    return False

def delete_at_tail(head):
    if(head is None or head.next is None):
        return None
    temp = head

    while(temp.next.next is not None):
        temp = temp.next
    
    temp.next = None
    return head




head = delete_at_tail(head)
print("After deletion")
print_LL(head)