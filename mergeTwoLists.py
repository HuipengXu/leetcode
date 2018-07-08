# 21. 合并两个有序链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        merge_list_node = ListNode(None)
        first_list = self.listnode_to_list(l1)
        second_list = self.listnode_to_list(l2)
        first_list.extend(second_list)
        merged_sorted_list = sorted(first_list)
        if len(merged_sorted_list) == 0:
            return []
        next_node = merge_list_node
        i = 0
        for num in merged_sorted_list:
            i += 1
            next_node.val = num
            if i == len(merged_sorted_list):
                break
            else:
                next_node.next = ListNode(None)
            next_node = next_node.next
        return merge_list_node

    def listnode_to_list(self, list_node):
        if list_node != None:
            flag = 1
            lst = []
        else:
            return []
        while flag:
            if list_node.next == None:
                flag = 0
            lst.append(list_node.val)
            list_node = list_node.next

        return lst
