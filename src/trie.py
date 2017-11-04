


class Node:
    def __init__(self, word):
        self.word = word
        self.child = dict()
        self.exist = False
    
    def get_child(self, word):
        return self.child.get(word)


class Trie:
    def __init__(self):
        self.root = Node(word="")

    def insert(self, phrase):
        current_node = self.root

        for word_index in range(len(phrase)):
            word = phrase[word_index]
            if not current_node.get_child(word):
                current_node.child[word] = Node(word)
            current_node = current_node.child.get(word)

        current_node.exist = True


    def search(self, phrase):
        current_node = self.root

        for word_index in range(len(phrase)):
            word = phrase[word_index]
            word_node = current_node.get_child(word)
            if word_node == None:
                return False
            current_node = word_node

        return current_node.exist


if __name__ == '__main__':
    trie = Trie()
    trie.insert('皇')
    trie.insert('皇帝')
    trie.insert('皇冠')
    trie.insert('皇上')
    trie.insert('皇上萬歲萬歲萬萬歲')
    trie.insert('天大地大')
    trie.insert('天空')
    trie.insert('勞神')
    trie.insert('勞心')
    trie.insert('費力')
    trie.insert('勞神費力')

    print(trie.root.child.get('勞').child)
    print(trie.search('皇上萬歲萬歲萬萬歲歲歲'))
    print(trie.search('勞神費'))
    print(trie.search('天'))