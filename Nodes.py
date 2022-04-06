class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node = ListNode(1, None)
node = ListNode(2, node)
node = ListNode(3, node)
node = ListNode(4, node)
node = ListNode(5, node)


# class Solution1:
#     """ returns middle node of a linked list """
#     def middleNode(self, head: [ListNode]) -> [ListNode]:
#         counter = 0
#         mid_node_nr = 0
#         mid_node = head
#         last_node = head
#         while last_node.next is not None:
#             last_node = last_node.next
#             if counter // 2 >= mid_node_nr:
#                 mid_node_nr += 1
#                 mid_node = mid_node.next
#             counter += 1
#         return mid_node.val
#
#
# print(Solution1().middleNode(node))


class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        count = 0
        node = head
        while node is not None:
            node = node.next
            count += 1

        node = head
        for _ in range(count - n):
            node = node.next
        node = node.next.next
        while node.next is not None:
            node = node.next
        return node


print(Solution().removeNthFromEnd(node, 2))
