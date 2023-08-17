
class Trie:
    def __init__(self):
        self.all_nodes = []
        self.all_edges = []
        self.root = self.add_node()

    class node:
        def __init__(self):
            self.label = None
            self.edges = []
            self.indicator = None

    class edge:
        def __init__(self):
            self.from_node = None
            self.target_node = None
            self.label = None
            self.position = None
    
    def add_node(self):
        newNode = Trie.node()
        newNode.label = len(self.all_nodes)
        self.all_nodes.append(newNode)
        return newNode

    def add_edge(self, from_node, target_node, lbl, pos = None):
        newEdge = Trie.edge()
        newEdge.from_node = from_node
        newEdge.target_node = target_node
        newEdge.label = lbl
        newEdge.position = pos
        from_node.edges.append(newEdge)
        self.all_edges.append(newEdge)
        return newEdge

def trie_construction(pattern_list):
    trie = Trie()
    for pattern in pattern_list:
        current = trie.root
        for char in pattern:
            for edge in current.edges:
                if edge.label == char:
                    current = edge.target_node
                    break
                else:
                    new_node = trie.add_node()
                    trie.add_edge(current, new_node, char)
                    current = new_node
    return trie


if __name__ == "__main__":
    pattern_list = ['ATAGA','ATC', 'GAT']
    # with open("rosalind_ba9a.txt", "r") as f:
    #     pattern_list = []
    #     for line in f.readlines():
    #         print(line)
    #         pattern_list.append(line.strip())
    trie = trie_construction(pattern_list)
    for edge in trie.all_edges:
        print(str(edge.from_node.label) + '->' + str(edge.target_node.label) + ':' + str(edge.label))



#  #store the result in a txt file if the input is large.
# if __name__ == "__main__":
#     with open("rosalind_ba9a.txt", "r") as f:
#         pattern_list = [line.strip() for line in f.readlines()]

#     trie = trie_construction(pattern_list)

#     with open("output.txt", "w") as output_file:
#         for edge in trie.all_edges:
#             output_file.write(str(edge.from_node.label) + '->' + str(edge.target_node.label) + ':' + str(edge.label) + '\n')

#     print("Output written to 'output.txt'.")
        

