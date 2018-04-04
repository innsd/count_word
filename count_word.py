import error_handling
import handle_word
import c_io
import re
import operator
filename='testfile.dat'
contents=''
try:
    with open(filename) as f:
        contents=f.read()
except FileNotFoundError as e:
    error_handling.deal_file_not_found()
else:
    #记录日志，打开文件成功
    pass
#print(contents)
word_list=re.split(r'[\s\]\[\(\)\.\,]+',contents)
print(word_list)
word_list=list(filter(handle_word.is_normal_word,word_list))
handle_word.standardizing(word_list)
print(word_list)
word_dict={}
for word in word_list:#形成字典word_dict
    try:
        word_dict[word]['times']+=1
    except KeyError as e:
        word_dict[word]={'times':1,'explains':[]}
print(word_dict)
handle_word.translate(word_dict)#使用有道API翻译
sorted_words=dict(sorted(list(word_dict.items()),key=lambda item:item[1]['times'],reverse=True))
print(sorted_words)
print(repr(sorted_words))
c_io.save_as_json(sorted_words)
    #接下来的计划：使用API进行翻译
    #词源归纳