[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **DEDA_class2019_SYSU_Abstract_LDA_wordcloud** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: DEDA_class2019_SYSU_Abstract_LDA_wordcloud

Published in:  LN_SDA_2019

Description: Create a word cloud picture to make a short description of 130 abstracts

Keywords: word cloud, topic modelling, abstract analysis

See also: SL_2019_alpha_centauri_pirates_wordcloud

Author: FB, FS

```

![Picture1](qletlogo_tr.png)

![Picture2](wordcloud_abstract.png)

### PYTHON Code
```python

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


```

automatically created on 2019-09-10