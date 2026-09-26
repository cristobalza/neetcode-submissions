class Node:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:

            if ch not in curr.children:
                curr.children[ch] = Node()

            curr = curr.children[ch]

        curr.isEnd = True
        

    def search(self, word: str) -> bool:

        def dfs(i, node):
            curr = node

            for j in range(i, len(word)):
                ch = word[j]

                if ch == ".":
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True 
                    
                    return False

                else:
                    if ch not in curr.children:
                        return False
                    
                    curr = curr.children[ch]

            return curr.isEnd

        return dfs(0, self.root)
