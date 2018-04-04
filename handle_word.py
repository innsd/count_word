import re
import requests
import hashlib
import sys
import json
import c_io
from random import randint
class Http_Error(Exception):
    pass
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
def translate(words_dict):
    youdao_app_ID='557fea7e5b972442'
    youdao_app_Key='8bHiB3pPIMxrvkrUtXCR2l9EltCURHeu'
    from_language='auto'
    to_language='zh_CHS'
    urlpr={}
    for word in words_dict.keys():
        r_Num=str(randint(0,9))
        md5_obj=hashlib.md5()
        md5_obj.update((youdao_app_ID+word+r_Num+youdao_app_Key).encode('utf-8'))
        urlpr['q']=word
        urlpr['from']=from_language
        urlpr['to']=to_language
        urlpr['appKey']=youdao_app_ID
        urlpr['salt']=r_Num
        urlpr['sign']=str(md5_obj.hexdigest()).upper()
        try:
            r=requests.get('http://openapi.youdao.com/api?',urlpr)
            if(r.status_code!=200):
                raise Http_Error("URL连接异常")
        #r=requests.get("http://openapi.youdao.com/api?q=good&from=EN&to=zh_CHS&appKey=557fea7e5b972442&salt=2&sign=A95EA6F6230FC33934E5E1FE810FAC76")
            r.encoding=r.apparent_encoding
            #debug-code print(r.text)
            data=json.loads(r.text)
            #debug-code print(repr(data)) print("===========") print(data['basic']['explains'])
            words_dict[word]['explains']=(data['basic']['explains'])
            print('get %s successfully(explains)'%word)
            #for i in range(len(words_dict[word][1])):
            #    words_dict[word][1][i]=words_dict[word][1][i].encode('utf-8').decode('utf-8')
        except Http_Error as eu:
            print('url get error:'+r.url+r.text)
            print(eu)
        except KeyError:
            try:
                words_dict[word]['explains']=(data['translation'])
                print('get %s successfully(translation)'%word)
            except KeyError as ek:
                print('Error! word:%s URL:%s text:%s'%(word,r.url,r.text))
                print(ek)
if(__name__=='__main__'):
    test={'makler':{'times':1,'explains':[]}}
    translate(test)
    c_io.save_as_json(test)