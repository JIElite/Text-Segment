import dictionary 


print("----- Start to build Dictionary -----")

dict_1 = '../dictionray/dict_revised_2015_20160523/dict_revised_2015_20160523_1.xls'
dict_2 = '../dictionray/dict_revised_2015_20160523/dict_revised_2015_20160523_2.xls'
dict_3 = '../dictionray/dict_revised_2015_20160523/dict_revised_2015_20160523_3.xls'
dictionary = dictionary.Dictionary()
dictionary.expand_dictionary_by_xls(dict_1)
dictionary.expand_dictionary_by_xls(dict_2)
dictionary.expand_dictionary_by_xls(dict_3)
dictionary.save()

print("----- Finished! -----")