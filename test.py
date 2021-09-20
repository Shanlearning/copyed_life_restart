

import sys, os
os.chdir('C:\\Users\\zhong\\Dropbox\\github\\lifeRestart')
sys.path.append(os.getcwd())

from tqdm import tqdm
import json

_dat = json.loads(open('data\\age.json').read())

_dat = json.loads(open('data\\events.json',encoding="utf-8").read())


import re

for item in _dat:
    if "America" in _dat[item]['event']:
        print(_dat[item]['event'])
        print(item)


_dat["10702"]['event'] = 'The establishment of universal scoring standards for film and television music by elites has caused widespread controversy.'


for item in _dat:
    if "postEvent" in _dat[item]:
            print(_dat[item]['event'])

        if "US" in _dat[item]['postEvent']:
            print(_dat[item]['event'])
            print(item)

[_dat[item]['event'] for item in _dat]





list(_dat.keys())


_dat



from googletrans import Translator

#from google.cloud import translate_v2 as translate

import time

translator = Translator(service_urls=['translate.googleapis.com'])


for item in tqdm(list(_dat.keys())):
    result = translator.translate(_dat[item]['event'])    
    _dat[item]['event'] = result.text
    print(result.text)
    time.sleep(2)

with open('data\\events.json', 'w') as fp:
    json.dump(_dat, fp)  


from os import environ
from google.cloud import translate

sample_text = "Hello world!"
target_language_code = "en"


[_dat[item]['event'] for item in list(_dat.keys())[182:1000]],

content_list = [_dat[item]['event'] for item in list(_dat.keys())[1000:]]

response = client.translate_text(
    contents = content_list,
    target_language_code=target_language_code,
    parent=parent,
)

content_list = [translation.translated_text for translation in response.translations]

for i in range(len(list(_dat.keys())[1000:])):
    _dat[list(_dat.keys())[1000:][i]]['event'] = content_list[i]
    
    
[_dat[item]['event'] for item in list(_dat.keys())[182:1000]]








