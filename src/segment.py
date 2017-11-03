# -*- coding: utf-8 -*-
import xlrd
import pygtrie
import pickle


class Dictionary:
    def __init__(self):
        self.trie = pygtrie.StringTrie()

    def expand_dictionary_by_xls(self, dic_path):
        book = xlrd.open_workbook(dic_path)
        sh = book.sheet_by_index(0)
        
        for rx in range(sh.nrows):
            word = sh.cell_value(rx, 2)
            self.trie[word] = True
        
    def save(self, obj_path='../dictionray/dictionary_trie.pkl'):
        with open(obj_path, 'wb') as fd:
            pickle.dump(self.trie, fd)
    
    def load(self, obj_path='../dictionray/dictionary_trie.pkl'):
        with open(obj_path, 'rb') as fd:
            self.trie = pickle.load(fd)

    def search(self, word):
        return self.trie.get(word)


class DictionaryDoesNotExistError(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

class SegmentSystem:

    def __init__(self):
        self.dictionary = None
    
    def use_dictionary(self, dictionary):
        self.dictionary = dictionary

    def segments(self, input_sentence):
        if dictionary is None:
            raise DictionaryDoesNotExistError 

        segment_list = []
        word_start_index = 0
        current_processing_index = word_start_index
        finish_index = len(input_sentence)
        
        while current_processing_index != finish_index:
            matching = self.dictionary.search(input_sentence[word_start_index:current_processing_index+1])
            if not matching:
                maximum_matching_word = input_sentence[word_start_index:current_processing_index]
                segment_list.append(maximum_matching_word)
                word_start_index = current_processing_index
            current_processing_index += 1
        
        # The last phrase
        maximum_matching_word = input_sentence[word_start_index:current_processing_index]
        segment_list.append(maximum_matching_word)
 
        return segment_list




if __name__ == '__main__':
    dict_1 = '../dictionray/dict_revised_2015_20160523/dict_revised_2015_20160523_1.xls'
    dict_2 = '../dictionray/dict_revised_2015_20160523/dict_revised_2015_20160523_2.xls'
    dict_3 = '../dictionray/dict_revised_2015_20160523/dict_revised_2015_20160523_3.xls'
    
    dictionary = Dictionary()
    dictionary.load()
    # dictionary.expand_dictionary_by_xls(dict_1)
    # dictionary.expand_dictionary_by_xls(dict_2)
    # dictionary.expand_dictionary_by_xls(dict_3)
    # dictionary.save()

    segments_agent = SegmentSystem()
    segments_agent.use_dictionary(dictionary)
    segment_list = segments_agent.segments('麥當勞好好吃大便')
    print(segment_list)
