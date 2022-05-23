class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_node(vals: list) -> ListNode:
    node = None
    for i in range(len(vals)):
        node = ListNode(vals[i], node if node is not None else None)
    return node


node1 = create_node([1, 2, 3, 4, 5])
node2 = create_node([3, 7, 9, 3, 5, 8, 0])


class Solution:
    """ returns middle node of a linked list """

    def middleNode(self, head: [ListNode]) -> [ListNode]:
        counter = 0
        mid_node_nr = 0
        mid_node = head
        last_node = head
        while last_node.next is not None:
            last_node = last_node.next
            if counter // 2 >= mid_node_nr:
                mid_node_nr += 1
                mid_node = mid_node.next
            counter += 1
        return mid_node.val

    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        list_node_length = 0
        vals = []
        node = head
        while node is not None:
            vals.append(node.val)
            node = node.next
            list_node_length += 1
        vals.pop(list_node_length - n)
        vals.reverse()
        node = create_node(vals)
        return node


# print(Solution().middleNode(node))

node1 = Solution().removeNthFromEnd(node1, 2)
node2 = Solution().removeNthFromEnd(node2, 1)