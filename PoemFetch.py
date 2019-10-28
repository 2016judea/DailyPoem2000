"""
Author: Aidan Jude
Date: 10/28/2019
"""

from urllib.request import Request, urlopen
import json
import random
import requests

base_url = "https://thundercomb-poetry-db-v1.p.rapidapi.com/"
headers = {
    'x-rapidapi-host': "thundercomb-poetry-db-v1.p.rapidapi.com",
    'x-rapidapi-key': YOUR_API_KEY_HERE
    }
#API endpoints
author_end = "author"

def get_random_poem(max_lines):
    lines_len = 100
    while lines_len >= max_lines:
        authors = json.loads(requests.request("GET", base_url + author_end, headers=headers).text)
        author = authors['authors'][random.randint(0, len(authors['authors']) - 1)]
        poems = json.loads(requests.request("GET", base_url + author_end + '/' + author, headers=headers).text)
        ran_poem = random.randint(0, len(poems)-1)
        title = poems[ran_poem]['title']
        lines = ''
        line = ''
        for x in range(0, int(poems[ran_poem]['linecount'])):
            line = poems[ran_poem]['lines'][x]
            lines += ('\n' + line)
        lines_len = int(poems[ran_poem]['linecount'])
    
    return author, title, lines
