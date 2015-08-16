from timeit import Timer
import sys
sys.path.append('../Trie')
from src.Trie import Trie

def firstInsertion():
    trie = Trie()
    trie.insert("gaurav")

setup = "from __main__ import firstInsertion"
t = Timer("firstInsertion()", setup=setup)
print "\nfirst insertion 1000 times"
print t.repeat(3,1000)

def existingInsertion():
    trie = Trie()
    trie.insert("gaurav")
    trie.insert("gann")
    trie.insert("gannt")

setup = "from __main__ import existingInsertion"
t = Timer("existingInsertion()", setup=setup)
print "\nexisting insertion 1000 times"
print t.repeat(3,1000)

def deletion():
    trie = Trie()
    trie.insert("gaurav")
    trie.insert("gann")
    trie.insert("gannt")
    trie.delete("gann")

setup = "from __main__ import deletion"
t = Timer("deletion()", setup=setup)
print "\ndeletion 1000 times"
print t.repeat(3,1000)

def nonExistingDeletion():
    trie = Trie()
    trie.insert("gaurav")
    trie.insert("gann")
    trie.insert("gannt")
    trie.delete("gan")

setup = "from __main__ import nonExistingDeletion"
t = Timer("nonExistingDeletion()", setup=setup)
print "\nnon Existing deletion 1000 times"
print t.repeat(3,1000)
