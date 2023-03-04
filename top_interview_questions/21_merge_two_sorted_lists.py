#!/usr/bin/env python3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

    if len(list1) == 0 and len(list2) == 0:
        return ListNode(val="", next=None)


    lista = []

    while list1.next != None:
        lista.append(list1.val)
        list1 = list1.next

    while list2.next != None:
        lista.append(list2.val)
        list2 = list2.next


    lista = sorted(lista)

    root = arrayToList(lista, len(list))
    return root
    

def insert(root, item):
    temp = ListNode(item)
      
    if (root == None):
        root = temp
    else:
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
      
    return root

def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])
      
    return root


def main():
    print("Py3")

##############################################################################

if __name__ == "__main__":
    main()