class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Tries:
    def __init__(self):
        self.head = Node(None)
        
    def insert(self, string):
        curr_node = self.head
        
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            if curr_node.data != None:
                return True
        curr_node.data = string
        return False
    
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    trie = Tries()
    n = int(input())
    arr = [input().rstrip().replace(" ", "") for _ in range(n)]
    arr.sort()
    
    flag = 0
    for string in arr:
        if trie.insert(string):
            flag = 1
            break
    
    print("NO" if flag else "YES")