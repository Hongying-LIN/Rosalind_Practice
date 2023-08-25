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

def trie_matching(text, patterns):
    root = TrieNode()
    for pattern in patterns:
        insert_word(root, pattern)
    
    positions = []
    for i in range(len(text)):
        if prefix_trie_matching(text[i:], root):
            positions.append(i)
    
    return positions

def prefix_trie_matching(text, root):
    node = root
    for i, char in enumerate(text):
        if char in node.children:
            node = node.children[char]
            if node.is_end_of_word:
                return True
        else:
            return False
    return False

# Sample Dataset
text = "AATCGGGTTCAATCGGGGT"
patterns = ["ATCG", "GGGT"]
# with open("rosalind_ba9b.txt", "r") as f:
#     lines = f.read().splitlines()
#     text = lines[0]
#     patterns= []
#     for i in range(1, len(lines)):
#         patterns.append(lines[i])

# Find matching positions
matching_index = trie_matching(text, patterns)
print(" ".join(map(str, matching_index)))
 
 







 