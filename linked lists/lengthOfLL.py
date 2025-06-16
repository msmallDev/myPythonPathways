from takeInput import Node, take_input, print_LL


def lengthofLL(head):
    temp = head
    ans = 0

    while (temp != None):
        temp = temp.next
        ans = ans + 1

    return ans

headofLL = take_input()
length = lengthofLL(headofLL)
print(length)


def lengthOfLinkedListRecursive(head):
    if(head==None):
        return 0
    
    recursionAnswer = lengthOfLinkedListRecursive(head.next)
    return 1 + recursionAnswer

length = lengthOfLinkedListRecursive(headofLL)
print(length)