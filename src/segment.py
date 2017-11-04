# -*- coding: utf-8 -*-
import dictionary


class SegmentSystem:
    def __init__(self):
        self.dictionary = None
    
    def use_dictionary(self, dictionary):
        self.dictionary = dictionary

    def segments(self, input_sentence):
        if self.dictionary is None:
            raise dictionary.DictionaryDoesNotExistError

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