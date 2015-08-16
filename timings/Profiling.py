import profile
import sys
sys.path.append('../Trie')
from src.Trie import Trie

t = Trie()
print "profiling for new insert"
profile.run('t.insert("gaurav")')
t.insert("gann")

print "profiling for inserting gannt when gann exisits"
profile.run('t.insert("gannt")')
t.insert("usa")
t.insert("us")

print "profiling for deleting gannt"
profile.run('t.delete("gannt")')
t.insert("gannt")


