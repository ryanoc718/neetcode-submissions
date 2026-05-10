class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def backtrack(node, part):
            for p in range(len(part)):
                if part[p] != ".":
                    if part[p] not in node.children:
                        #print("0")
                        return False
                    node = node.children[part[p]]
                else:
                    if p == len(part)-1:
                        for key in node.children:
                            if node.children[key].endOfWord:
                                return True
                        return False
                    for key in node.children:
                        #print(node.children, part[p+1:])
                        if backtrack(node.children[key], part[p+1:]):
                            #print("1.5")
                            return True
                    #print("2")
                    return False
            #print("3", node.endOfWord)
            return node.endOfWord 
        return backtrack(self.root, word)        




