# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        current = head
        carry = 0

        while l1 != None and l2 != None:
            value = l1.val + l2.val + carry
            if value < 10:
                carry = 0
            else:
                carry = 1
            newNode = ListNode(value % 10)
            current.next = newNode
            current = newNode

            l1 = l1.next
            l2 = l2.next

        l3 = l1 if l1 else l2
        while l3 != None:
            value = l3.val + carry
            if value < 10:
                carry = 0
            else:
                carry = 1
            newNode = ListNode(value % 10)
            current.next = newNode
            current = newNode
            l3 = l3.next

        if carry == 1:
            newNode = ListNode(1)
            current.next = newNode
            current = newNode

        return head.next
