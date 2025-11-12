from typing import Any

class LinkNode:
    def __init__(self, val: Any, last:LinkNode=None, next: LinkNode=None):
        self.val = val
        self.last = last
        self.next = next

    def from_linknode_to_list(self, head: LinkNode):
        final_list = []
        final_list.append(head.val)
        while head.next: 
            head = head.next
            final_list.append(head.val)
        return final_list
    
    def from_list_to_linknode(self, lst: list):
        new_linknode = LinkNode(lst[0])
        head = new_linknode
        for i in range(1, len(lst)):
            new_linknode.next = LinkNode(lst[i])
            new_linknode.last = new_linknode
            new_linknode = new_linknode.next
        return head



l1 = LinkNode(0)
l1.next = LinkNode(1)
l1.last = l1
l1.next.next = LinkNode(2)
l1.next.last = l1.next
l1.next.next.next = LinkNode(3)
print(l1.from_linknode_to_list(l1))
print(l1.next.next.val)
print(l1.from_list_to_linknode([1,2,3,4,5,]))        
