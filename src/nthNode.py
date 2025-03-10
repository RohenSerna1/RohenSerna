class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

    def list_to_linked_list(lst):
        dummy = ListNode(0)
        current = dummy
        for number in lst:
            current.next = ListNode(number)
            current = current.next

        return dummy.next
    
    def linked_list_to_list(node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        
        return lst

def removeNthFromEnd(head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next