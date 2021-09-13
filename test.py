

import sys, os
os.chdir('C:\\Users\\zhong\\Dropbox\\github\\lifeRestart')
sys.path.append(os.getcwd())

from tqdm import tqdm
import json

_dat = json.loads(open('data\\age.json').read())

_dat = json.loads(open('data\\events.json',encoding="utf-8").read())

from googletrans import Translator

translator = Translator(service_urls=['translate.googleapis.com'])
for item in tqdm(_dat):
    _dat[item]['event'] = translator.translate(_dat[item]['event'], dest='en').text




