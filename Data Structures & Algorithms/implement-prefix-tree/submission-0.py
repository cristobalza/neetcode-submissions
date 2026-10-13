class TrieNode:
    def __init__(self, isEnd: bool = False, children: list = [None] * 26):
        self.isEnd = isEnd
        self.children = children

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            
            i = ord("a") - ord(c)
            if curr.children[i] is None:
                curr.children[i] = TrieNode()

            curr = curr.children[i]

        curr.isEnd = True


    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            i = ord("a") - ord(ch)
            if curr.children[i] is None:
                return False

            curr = curr.children[i]

        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for ch in prefix:
            i = ord("a") - ord(ch)

            if curr.children[i] is None:
                return False

            curr = curr.children[i]

        return True
        
        