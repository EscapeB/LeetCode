import math
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def array2tree(array) -> TreeNode or None:
    if len(array) == 0:
        return None
    else:
        root = TreeNode(array[0])
        node_array = [None] * len(array)
        for i in range(len(array)):
            if i == 0:
                node_array[i] = root
                continue
            else:
                if array[i]:
                    node_array[i] = TreeNode(array[i])
                    pos = math.floor((i - 1) / 2)
                    remain = (i - 1) % 2
                    if remain == 0:
                        node_array[pos].left = node_array[i]
                    elif remain == 1:
                        node_array[pos].right = node_array[i]
        return root


def array2linked(array) -> ListNode:
    if len(array) == 0:
        return
    root = ListNode(array[0])
    p = root
    for index in range(len(array)):
        if index == 0:
            continue
        else:
            p.next = ListNode(array[index])
            p = p.next
    return root


def liked2array(head: ListNode) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def printDoubleArray(arr: List[List]) -> None:
    for i in range(len(arr)):
        print(arr[i], '\n')
