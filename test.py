

import sys, os
os.chdir('C:\\Users\\zhong\\Dropbox\\github\\lifeRestart')
sys.path.append(os.getcwd())

from tqdm import tqdm
import json

_dat = json.loads(open('data\\age.json').read())

_dat = json.loads(open('data\\events.json',encoding="utf-8").read())

from googletrans import Translator

#from google.cloud import translate_v2 as translate



translator = Translator(service_urls=['translate.googleapis.com'])
for item in tqdm(_dat):
    _dat[item]['event'] = translator.translate(_dat[item]['event'], dest='en').text

result = translator.translate(_dat[item]['event'])

result.text

_dat[list(_dat.keys())[120]]

with open('data\\events.json', 'w') as fp:
    json.dump(_dat, fp)  
            