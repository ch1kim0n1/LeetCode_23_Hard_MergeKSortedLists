import heapq

class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        curr = dummy
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, id(node), node))
        while heap:
            _, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))
        return dummy.next
