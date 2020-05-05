#Josue Andaluz
#190250
# CISC 160-XX
# Lab 04
#worked with megan and kamerrie


from Binary_Node import BinaryNode



'''
Function which takes the root node of a sorted binary tree and an element.
  This function finds where in the binary tree that the element should be
  inserted (by using the algorithm provided in the lab booklet) so that the
  the tree stays in order.
PARAM:   root_node      The root of the linked list
PARAM:   new_element    The new element to be added into the list
RETURNS: The node at the root of the sorted binary tree.
'''
def insert(root_node, new_element):
    if root_node is None:
        root_node = BinaryNode(new_element)
        return root_node
    


    current = root_node

        
    while True:
        if new_element >= current.get_element():
            if current.get_right() is not None:
                current = current.get_right()

            else:
                
                current.set_right(BinaryNode(new_element,current))

                return root_node

        if new_element < current.get_element():
            if current.get_left() is not None:
                current = current.get_left()


            else:
                current = current.set_left(BinaryNode(new_element,current))

                return root_node
    
'''
Function which takes the root node of a binary tree and prints the tree using
  inorder traversal. Inorder traversal prints the left subtree first, then
  prints the element in the current node, then prints the right subtree.
PARAM:   root_node      The root of the linked list
'''

def _print_tree_inorder(root_node):


    
    if root_node.get_left() is not None:
        (_print_tree_inorder(root_node.get_left()))

    print(root_node.get_element())

    

    if root_node.get_right() is not None:
        (_print_tree_inorder(root_node.get_right()))



'''
Function which takes the root node of a sorted binary tree and an element.
  This function searchs the tree for that element using an iterative
  methodology. As it goes, the function creates a path of element in the nodes
  traversed and returns that path at the end.
PARAM:   root_node      The root of the linked list
PARAM:   element        The element to be found in the tree
RETURNS: The path through the tree from the root to the element's node, or
           None if the element cannot be found in the tree.
'''

def iterative_path(root_node, element):
    if root_node is None:
        return None

    path = " "

    current = root_node

        
    while True:
        if current.get_element() == element:
            path = path+" "+str(current.get_element())
            return path
          

        elif current.get_element() > element:
            if current.get_left() is None:
                return None
            else:
                path = path+" "+str(current.get_element())
                current = current.get_left()

        
        
        else:
            current.get_element() < element
            if current.get_right() is None:
                return None
            else:
               
                path = path+" "+str(current.get_element())
                current = current.get_right()

          

'''
Function which takes the root node of a sorted binary tree and an element.
  This function searchs the tree for that element using a recursive
  methodology. As it goes, the function creates a path of element in the nodes
  traversed and returns that path at the end.
PARAM:   root_node      The root of the linked list
PARAM:   element        The element to be found in the tree
RETURNS: The path through the tree from the root to the element's node, or
           None if the element cannot be found in the tree.
'''
def recursive_path(root_node, element):
    if root_node is None:
        return None
    
    if root_node.get_element() is element:
        return str(root_node.get_element())
    
    
    elif element < root_node.get_element():
        temp = recursive_path(root_node.get_left(), element)
        if temp is None:
            return None

        
        else:
            temp = str(root_node.get_element()) + " " + temp
            return temp
        



    else:
        element > root_node.get_element()
        temp = recursive_path(root_node.get_right(), element)
        if temp is None:
            return None

        
        else:
            temp = str(root_node.get_element()) + " " + temp
            return temp


        
        
            
        
        
