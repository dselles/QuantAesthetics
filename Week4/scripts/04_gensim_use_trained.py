import logging
import os

from gensim.models import KeyedVectors

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
this_dir = os.path.dirname(os.path.abspath(__file__))

custom_model_name = 'dance_of_death.kv'
model : KeyedVectors = KeyedVectors.load(custom_model_name, mmap='r')


#find most similar words
word = 'money'

sim_words = model.most_similar(word, topn=10)

print(f"the most similar words to {word} are:")

for w in sim_words:
    print(w)