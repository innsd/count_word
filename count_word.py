import error_handling
import handle_word
import re
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