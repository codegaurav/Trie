# Trie
Trie data structure

Python implementation for Trie code block. Read more about Trie here: https://en.wikipedia.org/wiki/Trie

###Using the Code
```python
trie = Trie("")

trie.insert("mumbai") #inserting into Trie

trie.delete("mumbai") #deleting from Trie

trie.printTrie()      #printing the entire Trie structure
```

#####Lookup
To check if the word exists in the Trie or not
```python
trie._lookup("mumbai",trie.root)
```
>Returns True or False

###Code Profiling
######individual function timings
```
python timings/Timings.py
```
>Run it from the parent directory Trie

######detailed function timings
```
python timings/Profiling.py
```
>Run it from the parent directory Trie


###Running the Tests
```
python tests/Testcases.py
```

>For verbosity
```
python tests/Testcases.py -v
```
