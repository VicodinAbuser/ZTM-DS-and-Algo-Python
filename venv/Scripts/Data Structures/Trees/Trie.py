#Trie is an efficient information reTrieval data structure.
#It is mostly used for searching through strings to see if certain desired words are present or not
#Doing this task using a list, or a balanced BST, costs O(nm) and O(mlog N) respectively, where m is the length of the string being searched
#But using tries, it can be done in O(m) time.
#Tries are like trees, with each node having multiple branches, generally equal to the number of letters in the alphabet.
#Each node represents a single letter. Each node also consists of an end_of_word variable which tells us whether it marks the end of a word or not
#Here we will implement two of its major operations, insert and search, both of which are of O(m)time complexity


#First we define a Trie_node class containing 26 children each initialized to None, and an end_of_word flag to determine whether it marks the end of a word or not
class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.is_end_of_word = False

#Next we define the Trie class itself containing a constructor which initializes the trie and the insert and search methods
class Trie():
    def __init__(self):
        self.root = TrieNode()

#We define a private helper function to calculate the numerical index of each character in the range of 0-25
    def _character_index(self, char):
        if char.isupper():
            return ord(char) - ord('A')
        else:
            return ord(char) - ord('a')

#Now we come to the insert function.
#We will create a pointer which will start at the root node. Then for every character in the word to be inserted,
#We will check if the character already exists in the trie by matching it with the pointer's children.
#If it does, we will simply update the pointer to that child of the current node and repeat the process for the next character of the word
#Otherwise, we will initialize a new node at the index of the character that is to be inserted, which was equal to None until now,
#And then we will update the pointer to point to this newly created node and repeat the process for the next character
#Once we reach the end of the word, we will set the is_end_of_word to True for the node containing the last character.
#The entire process will take O(m) time where m is the length of the string
    def insert(self, string):
        pointer = self.root
        for character in string:
            index = self._character_index(character)
            if not pointer.children[index]:
                pointer.children[index] = TrieNode()
            pointer = pointer.children[index]
        pointer.is_end_of_word = True
        return

#Finally, for the search method, we will follow the exact same approach
#Only this time, instead of creating a new TrieNode when we don't find a character in the Trie, we will simply return False
#And if after the loop terminates and is_end_of_word equals True and the node isn't equal to None, it means we have found the word
    def search(self, string):
        pointer = self.root
        for character in string:
            index = self._character_index(character)
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]
        return pointer and pointer.is_end_of_word


my_trie = Trie()
my_trie.insert('Data')
my_trie.insert("Structures")
my_trie.insert("and")
my_trie.insert("Algorithms")
print(my_trie.search("and"))
#True
print(my_trie.search("Data"))
#True
print(my_trie.search("woohoo"))
#False
print(my_trie.search("STructures"))
#True
