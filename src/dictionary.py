import pickle
import xlrd
import trie


class Dictionary:
    def __init__(self):
        self.trie = trie.Trie()
        self.max_len_for_each_word = dict()

    def expand_dictionary_by_xls(self, dic_path):
        book = xlrd.open_workbook(dic_path)
        sh = book.sheet_by_index(0)
        
        for rx in range(sh.nrows):
            phrase = sh.cell_value(rx, 2)
            self.trie.insert(phrase)
            
            phrase_start_word = phrase[0]
            longest = self.max_len_for_each_word.get(phrase_start_word)
            phrase_len = len(phrase)
            if not longest or longest < phrase_len:
                self.max_len_for_each_word[phrase_start_word] = phrase_len

    def save(self, obj_path='../dictionray/saved_dictionary.pkl'):
        with open(obj_path, 'wb') as fd:
            pickle.dump([self.trie, self.max_len_for_each_word], fd)

    def load(self, obj_path='../dictionray/saved_dictionary.pkl'):
        with open(obj_path, 'rb') as fd:
            (self.trie, self.max_len_for_each_word) = pickle.load(fd)

    def search(self, word):
        return self.trie.search(word)
    
    def get_longest_length_of_word(self, word):
        """ If not exist that starting word, it would return None """
        value = self.max_len_for_each_word.get(word)
        return value


class DictionaryDoesNotExistError(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)
