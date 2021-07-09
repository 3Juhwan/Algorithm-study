class Tries:
    def __init__(self):
        self.head = {}
        
    def insert(self, arr):
        curr_node = self.head
        
        for string in arr:
            if string not in curr_node:
                curr_node[string] = {}
            curr_node = curr_node[string]
        curr_node['End'] = {}
        
    def printStruct(self, node, length):
        curr_node = self.head if length == 0 else node

        for string in sorted(curr_node):
            if string == 'End': continue
            print("--" * length + string)
            if curr_node[string]:
                self.printStruct(curr_node[string], length + 1)

n = int(input())
trie = Tries()
for _ in range(n):
    arr = list(input().split())[1:]
    trie.insert(arr)

trie.printStruct(None, 0)