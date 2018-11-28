class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Flatten the tree into an array using depth first search 
# then represent the array as a string sperated by a special character. 
# Limits nodes can not contain
# the special character (in this case a space).
def serialize1(node):
    return " ".join(dfs(node))

def dfs(node):
    array = []
    if node.val == None:
        return array
    not_visited = [node]
    while(not_visited):
        visit = not_visited.pop(0)
        array.append(visit.val)
        if visit.left != None:
            not_visited.append(visit.left)
        if visit.right != None:
            not_visited.append(visit.right)
    return array

def deserialize1(tree):
    nodes = tree.split(" ")
    root = makeTree(0, nodes)
    return root		

def makeTree(node, nodes):
    if node >= len(nodes):
        return None
    left = makeTree(node*2 + 1, nodes)
    right = makeTree(node*2 + 1, nodes)
    return Node(nodes[node], left, right)

# Sets globals so that tests can call the desired implementation functions
serialize = None
deserialize = None
def soln1():
    global serialize, deserialize
    serialize = serialize1
    deserialize = deserialize1

# Test 1
def provided1():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    res = deserialize(serialize(node)).left.left.val == 'left.left'
    return res, 'left.left', deserialize(serialize(node)).left.left.val

def serialize_empty():
    node = Node(None)
    return serialize(node) == "", "", serialize(node)

def main():
    tests = {
        'provided1': provided1,
        'serialize_empty': serialize_empty,
    }
    test(tests, soln1)

def test(tests, func):
    print("Testing Function [{}]".format(func.__name__))
    func()
    for k,v in tests.items():
        res, expected, recieved = v()
        print("Passed" if res else "Failed", end=" ")
        print("Test [{}]: Expected {} Recieved {}".format(k, expected, recieved))

if __name__ == "__main__":
    main()

