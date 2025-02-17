# Python program to insert element in binary tree  
class newNode():  
  
    def __init__(self, data):  
        self.key = data 
        self.left = None
        self.right = None
          
""" Inorder traversal of a binary tree"""
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.key, end=" ")
    inorder(node.right)

  
"""function to insert element in binary tree """
def insert(root, key):
    if root.left and root.right:
        insert(root.left, key)
    elif root.left:
        root.right = newNode(key)
    else:
        root.left = newNode(key)
  
       
# Driver code
if __name__ == '__main__': 
    root = newNode(10)  
    root.left = newNode(11)  
    root.left.left = newNode(7)  
    root.right = newNode(9)  
    root.right.left = newNode(15)  
    root.right.right = newNode(8)  
  
    print("Inorder traversal before insertion:", end = " ") 
    inorder(root)
  
    key = 12
    insert(root, key)  
  
    print()  
    print("Inorder traversal after insertion:", end = " ") 
    inorder(root) 
