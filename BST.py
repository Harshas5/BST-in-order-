class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left: # if left node is not a leaf node alreayd had some data in it then
                self.left.add_child(data)
            else:           # if left node is leaf node  no left node i it

                self.left=BinarySearchTree(data)


        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)


    def InorderTraversl(self):
        elements= []
        if self.left: # visit left tereee first
            elements += self.left.InorderTraversl()

        elements.append(self.data) # visit base element

        if self.right: # visit right nodes
            elements += self.right.InorderTraversl()


        return elements

def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root



if __name__ == '__main__':
    numbers = [1, 4, 2, 5, 6, 89, 0, 3, 5, 6, 7, 8, 64]
    number_tree = build_tree(numbers)
    print(number_tree.InorderTraversl())


