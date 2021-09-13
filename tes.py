# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 07:23:02 2020

@author: zhong
"""
import sys, os
os.chdir('C:\\Users\\zhong\\Dropbox\\github\\lifeRestart')
sys.path.append(os.getcwd())

import json

dat = json.loads(open('data\\age.json').read()) 
dat = json.loads(open('data\\events.json', encoding='utf-8').read()) 
dat = json.loads(open('data\\talents.json', encoding='utf-8').read()) 



