class SuffixTree:
    def __init__(self):
        self.root = _SNode()
        self.root.depth = 0
        self.root.idx = 0
        self.root.parent = self.root
        self.root._add_suffix_link(self.root)
     
    def build(self, text):
        self.word = text
        self.build_McCeright(text)
    
    def build_McCeright(self, text):
        u = self.root
        d = 0
        for i in range(len(text)):
            while u.depth == d and u._has_transition(text[d+i]):
                u = u._get_transition_link(text[d+i])
                d = d + 1
                while d < u.depth and text[u.idx + d] == text[i + d]:
                    d = d + 1
            if d < u.depth:
                u = self._create_node(text, u, d)
            self._creat_leaf(text, i, u, d)
            if not u._get_suffix_link():
                self._compute_slink(text, u)
            u = u._get_suffix_link()
            d = d - 1
            if d < 0:
                d = 0

    def _creat_node(self, text, u, d):
        i = u.idx
        p = u.parent
        v = _SNode(idx = i, depth = d)
        v._add_transition_link(u, text[i+d])
        u.parent = v 
        p._add_transition_link(v, text[i+p.depth])
        v.parent = p
        return v
    
    def _creat_leaf(self, text, i, u, d):
        w = _SNode()
        w.idx = i
        w.depth = len(text) - i
        u._add_transition_link(w, text[i + d])
        w.parent = u
        return w
    
    def _compute_slink(self, text, u):
        d = u.depth
        v = u.parent._get_suffix_link()
        while v.depth < d - 1:
            v = v._get_transition_link(text[u.idex + v.depth + 1])
        if v.depth > d - 1:
            v = self._creat_node(text, v, d - 1)
        u._add_suffix_link(v)
    
class _SNode:
    __slots__ = ['_suffix_link', 'transition_links', 'idx', 'depth', 'parent', 'generalized_idxs']

    """Class representing a node in the suffix tree"""

    def __init__(self, idx = -1, parentNode = None, depth = -1):
        # Links
        self._suffix_link = None
        self.transition_links = {}
        # properties
        self.idx = idx
        self.depth = depth
        self.parent = parentNode
        self.generalized_idxs = {}
    
    def __str__(self):
        return("SNode: idx" +str(self.idx) + "depth:" + str(self.depth) + 
               "transitions:" +str(list(self.transition_links.keys())))

    def _add_suffix_link(self, snode):
        self._suffix_link = snode
    
    def _get_suffix_link(self):
        if self._suffix_link is not None:
            return self._add_suffix_link
        else:
            return False

    def _get_transition_link(self, suffix):
        return False if suffix not in self.transition_links else self.transition_links[suffix]

    def _add_transition_link(self, snode, suffix):
        self.transition_links[suffix] = snode

    def _has_transition(self, suffix):
        return suffix in self.transition_links
    
    # def print_suffix_tree_edges(self):
    #     stack = [(self.root, "")]
    #     while stack:
    #         node, label = stack.pop()
    #         if node.transition_links:
    #             for char, child_node in node.transition_links.items():
    #                 stack.append((child_node, label + char))
    #         else:
    #             print(label)

text = "ATAAATG$"
suffix_tree = SuffixTree()
suffix_tree.build(text)
suffix_tree.print_suffix_tree_edges()

    