class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

    def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data
    def Inorder(self):
        if(self.left):
            self.left.Inorder()
        print(self.data, end=' ')
        if(self.right):
            self.right.Inorder()
    
    def Preorder(self):
        print(self.data, end=' ')
        if(self.left):
            self.left.Preorder()
        if(self.right):
            self.right.Preorder()
    
    def Postorder(self):
        if(self.left):
            self.left.Postorder()
        if(self.right):
            self.right.Postorder()
        print(self.data, end=' ')
    def findX(self, x):
        if(self.data is None): return False
        if(self.data == x): return True
        if(self.data > x): return self.left.findX(x)
        if(self.data < x): return self.right.findX(x)

n = int(input('Nhap so cac phan tu: '))
x = int(input('Nhap phan tu: '))
binaryTree = Node(x)
for i in range(n-1):
    x = int(input('Nhap phan tu: '))
    binaryTree.insert(x)

binaryTree.Inorder()
print('\n')
binaryTree.Preorder()
print('\n')
binaryTree.Postorder()
print('\n')

X = int(input('Nhap X: '))
if(binaryTree.findX(x)): print('X co trong day')
else: print('X khong co trong day')
