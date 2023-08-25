class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True

def build_edges(root):
    edges = []
    
    def traverse(node, parent_id):
        for char, child in node.children.items():
            child_id = len(edges)+1
            edges.append((parent_id, child_id, char))
            traverse(child, child_id)
    
    traverse(root, 0)   
    return edges

# patterns to insert
patterns = ['ATAGA', 'ATC', 'GAT']
# with open("rosalind_ba9a.txt", "r") as f:
#     patterns = [line.strip() for line in f.readlines()]

# Build the trie
root = TrieNode()
for pattern in patterns:
    insert_word(root, pattern)

# Build edges list and convert to required format
edges = build_edges(root)
output = "\n".join(f"{parent}->{child}:{label}" for parent, child, label in edges)
print(output)

# with open("output.txt", "w") as output_file:
#     edges = build_edges(root)
#     output_file.write("\n".join(f"{parent}->{child}:{label}" for parent, child, label in edges))

# print("Output written to 'output.txt'.")