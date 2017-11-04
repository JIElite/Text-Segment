# -*- coding: utf-8 -*-
import xlrd
import trie 
import pickle


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

class SegmentSystem:

    def __init__(self):
        self.dictionary = None
    
    def use_dictionary(self, dictionary):
        self.dictionary = dictionary

    def segments(self, input_sentence):
        if self.dictionary is None:
            raise DictionaryDoesNotExistError 

        segment_list = []
        word_start_index = 0
        finish_index = len(input_sentence)
        
        while word_start_index != finish_index:
            remain_len = len(input_sentence[word_start_index:])
            longest_segment_len = self.dictionary.get_longest_length_of_word(input_sentence[word_start_index])
            if longest_segment_len is None:
                longest_segment_len = 1
            search_len = longest_segment_len if longest_segment_len < remain_len else remain_len
            maximum_matching = ""

            for length in range(search_len, 0, -1):
                searching_phrase = input_sentence[word_start_index:word_start_index+length]
                found_in_dict = self.dictionary.search(searching_phrase)
                if found_in_dict or length == 1:
                    # segment by maximum matching or just add word not existed in dict
                    maximum_matching = searching_phrase
                    segment_list.append(maximum_matching)
                    word_start_index = word_start_index + length
                    break
            
        return segment_list




# if __name__ == '__main__':
#     dict_1 = '../dictionray/dict_revised_2015_20160523/dict_revised_2015_20160523_1.xls'
#     dict_2 = '../dictionray/dict_revised_2015_20160523/dict_revised_2015_20160523_2.xls'
#     dict_3 = '../dictionray/dict_revised_2015_20160523/dict_revised_2015_20160523_3.xls'
    
#     dictionary = Dictionary()
#     # dictionary.load()
#     dictionary.expand_dictionary_by_xls(dict_1)
#     dictionary.expand_dictionary_by_xls(dict_2)
#     dictionary.expand_dictionary_by_xls(dict_3)
#     dictionary.save()

#     segments_agent = SegmentSystem()
#     segments_agent.use_dictionary(dictionary)

#     context = '''勞神勞力又勞心勞費的勞什骨子喜歡勞什子嗎？'''
#     segment_list = segments_agent.segments(context)
#     print(segment_list)

