def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    final_str = ''
    final_str += str(l1.val)
    while l1.next:
        l1 = l1.next
        final_str = str(l1.val) + final_str
    final_str2 = ''
    final_str2 += str(l2.val)
    while l2.next:
        l2 = l2.next
        final_str2 = str(l2.val) + final_str2
    __sum = str(int(final_str) + int(final_str2))
    _sum = []
    for i in reversed(__sum):
        _sum.append(int(i))
    new_linknode = ListNode(_sum[0])
    head = new_linknode
    for i in range(1, len(_sum)):
        new_linknode.next = ListNode(_sum[i])
        new_linknode = new_linknode.next
    return head



def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode(0)
    current_node = dummy_head
    carry = 0
    while l1 is not None or l2 is not None or carry != 0:
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0
        total_sum = val1 + val2 + carry
        new_digit = total_sum % 10
        carry = total_sum // 10
        new_node = ListNode(new_digit)
        current_node.next = new_node
        current_node = current_node.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    return dummy_head.next