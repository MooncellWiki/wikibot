from wikibot import *
from config import *

token = login_wiki(username, password, api_url)

with open("title.txt", "r", encoding='utf-8') as f:
	f_str = f.read().splitlines()
	result = list()
	
	for line in f_str:
		purge_ret = purge(token, api_url, line)
		result.append(purge_ret)
		
with open("result.json", "w", encoding='utf-8') as f1:
	result = json.dumps(result, indent=4, ensure_ascii=False)
	f1.write(result)