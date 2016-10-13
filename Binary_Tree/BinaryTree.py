class BinaryTree():
    def __init__(self, data):
        self.right=None;
        self.left=None;
        self.data=data;
    def getLeftChild(self):
        return self.left;
    def getRightChild(self):
        return self.right;
    def setNodeValue(self, data):
        self.data=data;
    def getNodeValue(self):
        return self.data;
    def insertLeft(self, newNode):
        if self.left==None:
            self.left=BinaryTree(newNode);
        else:
            tree=BinaryTree(newNode);
            tree.left=self.left;
            self.left=tree;

    def insertright(self, newNode):
        if self.right==None:
            self.right=BinaryTree(newNode);
        else:
            tree=BinaryTree(newNode);
            tree.left=self.left;
            self.left=tree;


def printTree(tree):
    if tree != None:
        printTree(tree.getLeftChild());
        print(tree.getNodeValue());
        printTree(tree.getRightChild());
def testTree():
        myTree=BinaryTree("Yash");
        myTree.insertLeft("Srijan");
        myTree.insertright("Mohit");
        myTree.insertLeft("Rahul");
        myTree.insertLeft("Himanshu");
        myTree.insertright("Sanu");
        printTree(myTree);

testTree();