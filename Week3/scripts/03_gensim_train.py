
import logging
import os

from gensim.models import Word2Vec
from multiprocessing import cpu_count
import re

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
this_dir = os.path.dirname(os.path.abspath(__file__))

#use this script to train a word2vec model on a text file.
#the model will be saved in the same directory as the text file

#TODO_______________________parameters to set (only edit here)
#the input text file to train the model on
input_text_file = 'moby_dick.txt'
#the output file name for the model. the extension .kv is signifies a keyed vector file (that is a word2vec dictionary that maps words to vectors)
output_file = 'moby_dick.kv'
#the size of the word vectors. the higher the number the more accurate the model is (sort of more semantic resolution, differentiating distinct direcitons in the embedding vector space), but also the more computationally expensive and memory intensive when loaded
vector_size = 150
#the number of epochs to train the model. the training process is iterative.
#there is no hard rule for the number of epochs. the more the better, but the more epochs the longer it takes to train the model
#how many epochs you need depends on the size of the corpus. for small corpora generally you need more epochs
#start with 100 and then increase if you are not satisfied with the results
epochs = 50
#_______________________end of parameters to set

print('started parsing text file')
sentences = []
with open(input_text_file, 'r', encoding="utf-8") as f:
    for line in f:
        l = line.strip().lower()
        if len(l) != 0 :
            tokens = re.split('\W+',  l)
            sentences.append(tokens)

model = Word2Vec(
    sentences,              #dataset, 
    min_count = 0,          #ignore rare words
    workers=cpu_count(), 
    vector_size=vector_size,
    epochs= epochs          #more epochs for small corpus
    )
model.wv.save(output_file)

