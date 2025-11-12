def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    lst = []
    lst.append(head.val)
    while head.next:
        head = head.next
        lst.append(head.val)
    _len = len(lst)
    if _len == 1:
        return
    if len(lst) == n:
        lst.pop(0)
    new_linknode = ListNode(lst[0])
    head = new_linknode
    for i in range(1, len(lst)):
        if i == _len - n:
            continue
        new_linknode.next = ListNode(lst[i])
        new_linknode.last = new_linknode
        new_linknode = new_linknode.next
    return head