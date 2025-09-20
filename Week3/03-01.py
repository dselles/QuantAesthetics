#In-Class Tutorial, 9/15/25
import gensim
# import os
# import numpy as np
# import math

# import matplotlib.pyplot as plt #for plotting if needed

# Importing only the necessary modules for vectors
from gensim.models import KeyedVectors
import gensim.downloader

# To handle SSL certificate issues (if any) during model download. Especially on MacOS.
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

model_name = "glove-wiki-gigaword-50"
model: KeyedVectors = gensim.downloader.load(model_name)
print(f"Model '{model_name}' loaded successfully.")

#result = model.most_similar('whale', topn=10) #test similarity of whale to other words

# calculate king - man + woman -> queen
origin = model.get_vector('king', norm=True) # normalized vector for 'king' - so it's length is 1. Otherwise, the length of the vector would likely be proportional to the frequency of the word in the training corpus
vec_from = model.get_vector('man', norm=True)
vec_to = model.get_vector('woman', norm=True)

axis_vec = vec_to - vec_from

result_vec = origin + axis_vec
# this is the same as king + (woman - man)
# it constructs the man-woman axis and then moves along that axis from king to find the result

closest_words = model.similar_by_vector(result_vec, topn=10)

print(f'closest words: {closest_words}') #note that the closest word will be 'king' itself, but the second closest word should be 'queen'