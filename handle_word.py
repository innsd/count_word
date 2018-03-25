import re
def is_normal_word(word):#如果是普通单词返回True
    if word=='':
        return False
    if re.match(r'[a-zA-Z]*[^a-zA-Z]+',word):#匹配字符串中是否有除单词外的字符，有的话就不是普通单词
        #print('DEL')
        return False
    else:
        #print('OK')
        return True
def handle_plural(word):
    pass
    return word
def standardizing(words):
    for i in range(0,len(words)):
        words[i]=words[i].lower()
        words[i]=handle_plural(words[i])