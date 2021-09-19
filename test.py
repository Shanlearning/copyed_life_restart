

import sys, os
os.chdir('C:\\Users\\zhong\\Dropbox\\github\\lifeRestart')
sys.path.append(os.getcwd())

from tqdm import tqdm
import json

_dat = json.loads(open('data\\age.json').read())

_dat = json.loads(open('events.json',encoding="utf-8").read())

from googletrans import Translator

#from google.cloud import translate_v2 as translate

import time

translator = Translator(service_urls=['translate.googleapis.com'])


_dat[list(_dat.keys())[182]]['event']
list(_dat.keys())[182:][0]

for item in tqdm(list(_dat.keys())[182:]):
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


_dat

for item in tqdm(list(_dat.keys())[182:]):
    _dat[list(_dat.keys())[182]]['event']

list(_dat.keys())[182:][0]

for item in list(_dat.keys())[182:1000]:
    

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








