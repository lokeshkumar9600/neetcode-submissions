# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle_node = slow
        second = middle_node.next
        middle_node.next = None
        

        prev = None
        current = second
        while current:
            temp= current.next
            current.next = prev
            prev = current
            current = temp
        
        first = head
        second = prev

        while second:
            temp_first = first.next
            temp_second = second.next
            first.next = second
            second.next = temp_first
            first = temp_first
            second = temp_second
        
        
            
        





        
        