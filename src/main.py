import segment



if __name__ == '__main__':
    dict_1 = '../dictionray/dict_revised_2015_20160523/dict_revised_2015_20160523_1.xls'
    dict_2 = '../dictionray/dict_revised_2015_20160523/dict_revised_2015_20160523_2.xls'
    dict_3 = '../dictionray/dict_revised_2015_20160523/dict_revised_2015_20160523_3.xls'
    
    dictionary = segment.Dictionary()
    dictionary.load()
    # dictionary.expand_dictionary_by_xls(dict_1)
    # dictionary.expand_dictionary_by_xls(dict_2)
    # dictionary.expand_dictionary_by_xls(dict_3)
    # dictionary.save()

    segments_agent = segment.SegmentSystem()
    segments_agent.use_dictionary(dictionary)

    context = '''勞神勞力又勞心勞費的勞什骨子喜歡勞什子嗎？'''
    segment_list = segments_agent.segments(context)
    print(segment_list)