import json
filename_save_json='words.json'
def save_as_json(word_dict):
    with open(filename_save_json,'w+') as f:
        json.dump(word_dict,f,ensure_ascii=False,indent=4)