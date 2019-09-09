# -*- coding: utf-8 -*-

import requests # take the website source code back to you
import urllib # some useful functions to deal with website URLs
from bs4 import BeautifulSoup as soup # a package to parse website source code
import numpy as np # all the numerical calculation related methods
import re # regular expression package
import itertools # a package to do iteration works
import pickle # a package to save your file temporarily
import pandas as pd # process structured data
save_path = 'abstract\\' # the path you save your files
base_link = 'http://www.wiwi.hu-berlin.de/de/forschung/irtg/results/discussion-papers' # This link can represent the domain of a series of websites



request_result = requests.get(base_link, headers = {'Connection': 'close'}) # get source code
parsed = soup(request_result.content) # parse source code
tr_items = parsed.find_all('tr')
info_list = [];
for item in tr_items:
    link_list = item.find_all('td')
    try:
        paper_title = (link_list[1].text.strip())
        author = (link_list[2].text)
        date_of_issue = (link_list[3].text)
        abstract_link = (link_list[5].find('a')['href'])
        tmp_list = [paper_title,author,date_of_issue,abstract_link];
        info_list.append(tmp_list)
    except Exception as e:
        
        print(e)
        print(link_list[5])
        continue

f_all = open('Abstract_all.txt','w',encoding='utf-8')

for paper in info_list:
    print(paper[0])
    try:
        paper_abstract_page = requests.get(paper[3], headers = {'Connection': 'close'});
        if paper[3][-3:] == 'txt':
            abstract_parsed = soup(paper_abstract_page.content)
            main_part = abstract_parsed.find_all('div', attrs={'id':r'content-core'})[0].text.strip()
        if paper[3][-3:] == 'pdf':
            abstract_parsed = soup(paper_abstract_page.content)
            main_part = abstract_parsed.find_all('body')[0].text.strip()

        main_part = re.sub(r'.+?[Aa]bstract', 'Abstract', main_part)
        main_part = re.sub(r'JEL [Cc]lassification:.*', '', main_part)
        main_part = re.sub(r'[A-Za-z][0-9][0-9]?', '', main_part)
        main_part = re.sub('[\r\n]+', ' ', main_part)
        f = open(save_path+ re.sub('[^a-zA-Z0-9 ]', '',paper[0])+'.txt','w',encoding='utf-8')
        f.write(main_part)
        f_all.write(main_part+"\nSEP\n")
        f.close()
    except Exception as e:
        print(e)
        print(paper[3])
        continue
f_all.close()