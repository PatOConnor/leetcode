class ListNode:
  def __init__(self, val=0, next=None) -> None:
    self.val = val
    self.next = next


class Solution:

  def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    """ Thought Process 1: traverse through linked lists together
    and add to an integer, then convert the integer back into a linked list"""
    #converting linked lists to integer...
    s = 0
    mult = 1
    #runs until both l1 and l2 have null value
    while l1 or l2:
      if l1: 
        s += l1.val * mult
        l1 = l1.next
      if l2: 
        s += l2.val * mult
        l2 = l2.next
      mult *= 10

    #converting back into linked list...
    head = ListNode()
    node = head
    while s > 0:
      node.val = s % 10
      node.next = ListNode()
      node = node.next
    return head

  def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
    """Thought Process 2: Don't Convert From Linked List"""
    head = ListNode()
    traveling_node = head
    carryover = False
    #runs until both l1 and l2 have null value
    while l1 or l2:
      new_val = 1 if carryover else 0
      if l1: 
        new_val += l1.val
        l1 = l1.next
      if l2: 
        new_val += l2.val 
        l2 = l2.next
      if new_val >= 10:
        carryover = True
        new_val -= 10
      traveling_node.val = new_val
      traveling_node.next = ListNode()
      traveling_node = traveling_node.next   
    return head
