import unittest
import sys
sys.path.append('../Trie')
from src.Trie import Trie

class InsertionTest(unittest.TestCase):
    def setUp(self):
        self.t = Trie()
        self.t.insert("gaurav")
        self.t.insert("gann")
        self.t.insert("usa")
        self.t.insert("gannt")

    def test_insert_simple(self):
        self.assertTrue(self.t._lookup("gann",self.t.root))
        self.assertTrue(self.t._lookup("gaurav",self.t.root))
        self.assertTrue(self.t._lookup("usa",self.t.root))    
        self.assertTrue(self.t._lookup("gannt",self.t.root))     

    def test_insert_smallerword_of_existing_bigger_word(self):
        self.t.insert("us")
        self.assertTrue(self.t._lookup("us",self.t.root))
        self.assertTrue(self.t._lookup("usa",self.t.root))
    
    def test_insert_same_word(self):
        self.t.insert("gann")
        self.assertTrue(self.t._lookup("gann",self.t.root))

    def test_insert_empty_word(self):
        self.t.insert("")
        self.assertTrue(self.t._lookup("gann",self.t.root))
        self.assertTrue(self.t._lookup("gaurav",self.t.root))
        self.assertTrue(self.t._lookup("usa",self.t.root))
        self.assertTrue(self.t._lookup("gannt",self.t.root))

    def test_insert_empty_word_into_empty_trie(self):
        testTrie = Trie()
        testTrie.insert("")
        self.assertTrue(len(testTrie.root.children) == 0)

class DeletionTests(unittest.TestCase):
    def setUp(self):
        self.t = Trie()
        self.t.insert("gaurav")
        self.t.insert("gann")
        self.t.insert("usa")
        self.t.insert("gannt")   
 
    #deleting gann from bag of words
    def test_delete_simple(self):
        self.assertTrue(self.t._lookup("gann",self.t.root))
        self.t.delete("gann")
        self.assertFalse(self.t._lookup("gann",self.t.root))

    #delete gann but gannt is valid
    def test_delete_smaller_word(self):
        self.assertTrue(self.t._lookup("gann",self.t.root))
        self.t.delete("gann")
        self.assertFalse(self.t._lookup("gann",self.t.root))
        self.assertTrue(self.t._lookup("gannt",self.t.root))

    #deleting gannt but gann is valid
    def test_delete_bigger_word(self):
        self.assertTrue(self.t._lookup("gannt",self.t.root))
        self.t.delete("gannt")
        self.assertFalse(self.t._lookup("gannt",self.t.root))
        self.assertTrue(self.t._lookup("gann",self.t.root))

    #deleting word with similar starting letters. deleting gann by gaurav is valid
    def test_delete_similar_starting_letters(self):
        self.t.delete("gann")
        self.assertTrue(self.t._lookup("gaurav",self.t.root))
        self.assertFalse(self.t._lookup("gann",self.t.root))

    def test_delete_same_word_twice(self):
        self.assertTrue(self.t._lookup("gann",self.t.root))
        self.t.delete("gann")
        self.t.delete("gann")
        self.assertFalse(self.t._lookup("gann",self.t.root))
    
    def test_delete_word_not_in_Trie(self):
        self.t.delete("australia")
        self.assertTrue(len(self.t.root.children) == 2)

    def test_delete_word_empty_Trie(self):
        testTrie = Trie()
        testTrie.delete("australia")
        self.assertTrue(len(testTrie.root.children) == 0)

    def test_delete_word_not_identified_as_leaf(self):
        self.t.delete("gan")
        self.assertTrue(self.t._lookup("gann",self.t.root))

if __name__ == '__main__':
    unittest.main()
