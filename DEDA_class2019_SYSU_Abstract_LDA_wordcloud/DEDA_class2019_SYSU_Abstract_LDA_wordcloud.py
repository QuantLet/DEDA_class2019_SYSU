# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
import os
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import numpy as np

# Please change the working directory to your path!
#os.chdir("/Users/xinwenni/LDA-DTM/xmas_song") 
d = os.getcwd()

raw_text= open('Abstract_all.txt','r',encoding='utf-8').read()
raw_text = str(raw_text)
raw_text=  re.sub('\n',' ',raw_text)

cleantextprep = str(raw_text)


# keep only letters, numbers and whitespace
expression = "[^a-zA-Z0-9 ]" 
cleantextCAP = re.sub(expression, '', cleantextprep) # apply regex
cleantext = cleantextCAP.lower() # lower case 



text_file = open("Output_total.txt", "w")
text_file.write(str(cleantext))
text_file.close()


root_path = os.getcwd()

# Read the whole text.
with open(path.join(root_path, 'Output_total.txt'), 'r', encoding='utf-8', errors='ignore') as outout_file:
    text = outout_file.readlines()

# Mask
#xmas_tree_pic = np.array(Image.open(path.join(root_path, "xmas_tree2.png")))
ql_pic = np.array(Image.open('qletlogo_tr.png'))

# Optional additional stopwords
stopword = set(STOPWORDS)
stopword = stopword.union({'abstract','keywords','sep'})
# Construct Word Cloud
# no backgroundcolor and mode = 'RGBA' create transparency
wc = WordCloud(max_words=100, stopwords=stopword, mask=ql_pic, mode='RGBA', background_color=None)


# Pass Text
wc.generate(text[0])

# store to file
wc.to_file(path.join(root_path, "wordcloud_abstract.png"))



plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

