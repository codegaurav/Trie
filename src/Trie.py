class Node:

    def __init__(self, inpChar):
        self.char = inpChar
        self.leaf = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = Node('')

    def _lookup(self, word, node):
        if len(word) == 0:
            return node.leaf
        elif word[0] in node.children:
            return self._lookup(word[1:], node.children[word[0]])
        else:
            return False

    def insert(self, word):
        if len(word) != 0 and not self._lookup(word, self.root):
            self._insertIntoTrie(word, self.root)

    def _insertIntoTrie(self, word, node):
        if len(word) != 0 and word[0] in node.children:
            return self._insertIntoTrie(word[1:], node.children[word[0]])
        if len(word) == 0:
            node.leaf = True
        else:
            while len(word) != 0:
                newNode = Node(word[0])
                node.children[word[0]] = newNode
                word, node = word[1:], newNode

            node.leaf = True

    def delete(self, word):
        if len(word) != 0 and self._lookup(word, self.root):
            self._deleteFromTrie(word, self.root)

    def _deleteFromTrie(self, word, node):
        if len(word) != 0:
            if self._deleteFromTrie(word[1:], node.children[word[0]]):
                node.children.pop(word[0], None)
                return True if len(node.children) == 0 and not node.leaf else False
        else:
            node.leaf = False
            return True if len(node.children) == 0 else False

    def printTrie(self):
        self._printTrie(self.root)

    def _printTrie(self, node, symbol = ''):
        print 'root' if node.char == '' else \
                symbol + '->' + node.char + ' : LEAF' + '\n' if node.leaf else \
                    symbol + '->' + node.char + '\n'
        for k, v in node.children.items():
            self._printTrie(v, symbol + '  ') if v != None else None


if __name__ == '__main__':
    t = Trie()
    t.insert('us')
    t.insert('gann')
    t.insert('gannt')
    t.insert('usa')
    t.printTrie()
    
    g = Trie()
    g.printTrie()
    
    t.insert('gaurav')
    t.printTrie()
