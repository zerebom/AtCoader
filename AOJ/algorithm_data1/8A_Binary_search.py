'''
なぜかAOJ上でアクセプトされない。
8A~8Cまで全部実装している。
global変数でむりくりNodesを実装している
find,serachあたりはクラスにした方がいいかもしれない
'''
class Node:
    def __init__(self, parent, left, right, key):
        self.parent = parent
        self.left = left
        self.right = right
        self.key = key


def insert(key, root):
    insert_node = Node(None, None, None, key)
    x_parent = None
    x = root
    while x != None:
        x_parent = x
        # 探索先(x)が葉になるまで続く
        if insert_node.key < x.key:
            x = x.left
        else:
            x = x.right

    insert_node.parent = x_parent

    # Nodesが空の場合
    if x_parent == None:
        root = insert_node
    elif insert_node.key < x_parent.key:
        x_parent.left = insert_node
    else:
        x_parent.right = insert_node

    return root

def find(key,root):
    x = root
    #値が一致するか、ノードがなくなるまで続く
    while x != None and key!=x.key:
        if key<x.key:
            x=x.left
        else:
            x=x.right
    return x
def treeSuccessor(node):
    '''nodeを探す'''
    if x.right !=None:
        return treeMinimum(x.right)
        

def delete(key,root):
    delete_node=find(key,root)
    if delete_node.left==None or delete_node.right==None:
        candidate_node=delete_node
    else:
        candidate_node=treeSuccessor(delete_node)



def preParse(node):
    if node == None:
        return
    print('',' {0}'.format(node.key), end='')

    # print(" %d" % (node.key), end="")
    # print(u,end=' ')
    preParse(node.left)
    preParse(node.right)


def inParse(node):
    if node == None:
        return
    inParse(node.left)
    print('',' {0}'.format(node.key), end='')
    # print(" %d" % (node.key), end="")
    # print(u,end=' ')
    inParse(node.right)


MAX_NODES = 100001
Nodes = [Node(None, None, None,None) for _ in range(MAX_NODES)]
if __name__ == "__main__":

    num_of_nodes = int(input())
    node_data = []
    for _ in range(num_of_nodes):
        node_data.append(input().split(' '))

    root = None


    for n in node_data:
        if len(n)==2:
            operation,n=n
            n=int(n)
        else:
            operation=n[0]
        if operation == 'insert':
            root = insert(n, root)

        if operation == 'find':
            root = find(n, root)

        if operation == 'print':
            inParse(root)
            print('')
            preParse(root)
            print('')

