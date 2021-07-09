class Node(object):
    def __init__(self):
        self.children = {}
        
class Tries:
    def __init__(self):
        self.head = Node()
        
    def insert(self, arr):
        curr_node = self.head
        
        for string in arr:
            if string not in curr_node.children:
                curr_node.children[string] = Node()
            curr_node = curr_node.children[string]
        
    def printStruct(self, node, length):
        if length == 0: curr_node = self.head
        else: curr_node = node
        
        for string in sorted(curr_node.children):
            # print(string)
            # if not curr_node.children:
            print("--" * length, end='')
            print(string)
            if curr_node.children[string]:
                self.printStruct(curr_node.children[string], length + 1)

n = int(input())
trie = Tries()
for _ in range(n):
    _input = list(input().split())
    k = int(_input[0])
    arr = _input[1:]
    trie.insert(arr)

trie.printStruct(None, 0)