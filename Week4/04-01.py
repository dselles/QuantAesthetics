# In-Class Coding Workshop, Week 4
# Quantitative Aesthetics, Fall 2025
# David Selles

# kv_Vis

import numpy as np
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
import gensim.downloader

model_path = r'Week4/scripts/PrideAndPrejudice.kv' # path to the precomputed word embedding model file
model: KeyedVectors = KeyedVectors.load(model_path, mmap='r') # load the model in read-only mode to save memory

# this will print all the words in the model's vocabulary
# for word in model.index_to_key:
#     print(word)

east_w = 'happy'
west_w = 'sad'
north_w = 'hate'
south_w = 'love'

words = ["person", "money", "family", "marriage", "country"]

east_v = model.get_vector(east_w, norm=True)
west_v = model.get_vector(west_w, norm=True)
north_v = model.get_vector(north_w, norm=True)
south_v = model.get_vector(south_w, norm=True)

axis_x = east_v - west_v
axis_y = north_v - south_v

words_v = []

for w in words:
    v = model.get_vector(w, norm=True)
    words_v.append(v)

# plotting
fig, ax = plt.subplots(figsize=(10,8))

# for i in range(len(words)):
#     w = words[i]
#     v = words_v[i]

# for w, v in zip(words, words_v): # iterate over words and their corresponding vectors
#     x = np.dot(v, axis_x)
#     y = np.dot(v, axis_y)
#     ax.scatter(x, y)
#     ax.text(x+0.01, y+0.01, w, fontsize=12)

for i, w in enumerate(words): # iterate over words and their indices. Same as above comment.
    v = words_v[i]
    x = np.dot(v, axis_x)
    y = np.dot(v, axis_y)
    ax.scatter(x, y)
    ax.text(x+0.01, y+0.01, w, fontsize=12)

plt.show()