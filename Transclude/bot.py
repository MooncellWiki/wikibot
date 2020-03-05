# -*- coding: utf-8 -*-
import requests
import json
import time
from wikibot import *
from config import *
from push_cq import *

result = str()
list1 = list()
dict_t = {}
token = login_wiki(username, password, api_url)

with open("title.txt", "r") as f:
	f_str=f.read().splitlines()
	
	for line in f_str:
		page = transcludedin(token, api_url, line, "2|3")
		dict_t[line] = page
with open("result.json", "w") as f1:
	result = json.dumps(dict_t, indent=4, ensure_ascii=False)
	f1.write(result)