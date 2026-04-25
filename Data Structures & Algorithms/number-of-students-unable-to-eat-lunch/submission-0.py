class MyListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        count_0 = 0
        count_1 = 0

        for st in students:
            if st == 0:
                count_0 += 1
            else:
                count_1 += 1
        
        for sa in sandwiches:
             if sa == 0 and count_0 > 0:
                count_0 -= 1
             elif sa == 1 and count_1 > 0:
                count_1 -= 1
             else:
                break


        return count_0 + count_1



        