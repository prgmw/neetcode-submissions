# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        reverse = None

        stop = head
        part_2 = head

        # quebra a lista em duas partes
        while stop and stop.next:
            part_2 = part_2.next
            stop = stop.next.next

        aux = part_2.next
        part_2.next = None

        #inverte a segunda lista
        while aux:
            proximo = aux.next
            aux.next = reverse
            reverse = aux
            aux = proximo
        
        n1 = head
        r1 = reverse

        while n1 and r1:
            tmp1 = n1.next
            tmp2 = r1.next
            
            n1.next = r1
            r1.next = tmp1

            n1 = tmp1
            r1 = tmp2

            

