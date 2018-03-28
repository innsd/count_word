import error_handling
import handle_word
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
for word in word_list:
    try:
        word_dict[word]+=1
    except KeyError as e:
        word_dict[word]=1
print(word_dict)
sorted_words=sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)
for t in sorted_words:
    print(t)
    #接下来的计划：使用API进行翻译
    #词源归纳