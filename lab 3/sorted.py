# Josue Andaluz
# 190250
# CISC 160-XX
# Lab 03
# worked with megan and kameerie
'''
Function which takes the head Node of a sorted linked list and an element.
  This function finds where in the linked list that the element should be
  inserted so that the linked list stays in order.
PARAM:   head_node      The head of the linked list
PARAM:   new_element    The new element to be added into the list
RETURNS: The node at the head of the linked list.
'''
import random
from Node import Node


def insert_sorted(head_node, new_element):
    new_node = Node(new_element)
    current_node = head_node
    previous_node = head_node

    if head_node is None:
        head_node = new_node
        # print("none")
        return head_node
    elif new_node.get_element() <= head_node.get_element():
        head_node = new_node
        head_node.set_next(current_node)
        # print("newHead")
        return head_node
    else:
        '''current_node = current_node.get_next()'''
        while current_node is not None:
            if new_node.get_element() <= current_node.get_element():
                previous_node.set_next(new_node)
                new_node.set_next(current_node)
                # print("newInsert")
                return head_node
            elif current_node.get_next() is None:
                current_node.set_next(new_node)
                # print("newEndNode")
                return head_node
            else:
                # print("nextElement")
                previous_node = current_node
                current_node = current_node.get_next()


'''
Test code can go below if you want
'''

if __name__ == '__main__':
    returned_head = None
    head_node = None

    for i in range(10):
        random_num = random.randint(1, 101)
        returned_head = insert_sorted(head_node, random_num)
        # print("test")
        # print(returned_head.get_element())
        head_node = returned_head

    print("Head Node is: " + str(returned_head.get_element()))

    print("The linked list is as follows: ")
    while returned_head is not None:
        print(returned_head.get_element())
        returned_head = returned_head.get_next()
