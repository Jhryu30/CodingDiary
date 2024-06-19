from sys import setrecursionlimit
setrecursionlimit(10000)

class BinaryTree:
    def __init__(self,x,y,val,left=None,right=None):
        self.val = val
        self.x = x
        self.y = y
        self.left = left
        self.right = right

def build_tree(root,node):
    if node.x<root.x:
        if root.left is None:
            root.left = node
        else:
            build_tree(root.left,node)
    else:
        if root.right is None:
            root.right = node
        else:
            build_tree(root.right,node)

def preorder_search(node,path):
    if node is None:
        return
    path.append(node.val)
    preorder_search(node.left,path)
    preorder_search(node.right,path)
    

def postorder_search(node,path):
    if node is None:
        return
    postorder_search(node.left,path)
    postorder_search(node.right,path)
    path.append(node.val)
        

def solution(nodeinfo):
    answer = [[]]
    
    nodes = sorted([[x,y,i+1] for i,(x,y) in enumerate(nodeinfo)], key=lambda x:(-x[1],x[0]))
    node_trees = [BinaryTree(x,y,n) for x,y,n in nodes]
    root = node_trees[0]
    for node in node_trees[1:]:
        build_tree(root,node)
        
    pre_path, post_path = [], []
    preorder_search(root,pre_path)
    postorder_search(root,post_path)
    
    answer = [pre_path, post_path]
    
    return answer