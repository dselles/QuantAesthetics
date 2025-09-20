import gensim
import logging
import os
import numpy as np
import math

import matplotlib.pyplot as plt

from gensim.models import KeyedVectors
import gensim.downloader

#these are needed to avoid SSL certificate error when downloading models from gensim api. Especially on MacOS
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#this is needed to display logging information when loading the model in case of an error
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
this_dir = os.path.dirname(os.path.abspath(__file__))


#set to the name of the pretrained model that you want to use (use the list of available models in 01_gensim_list_pretrained_models.py as reference)
pretrained_model_name = 'glove-wiki-gigaword-50'

#loading a model (this will download the model if it is not already downloaded, so it may be slow first time you use it)
model : KeyedVectors = gensim.downloader.load(pretrained_model_name)


words = ['cat', 'dog', 'animal', 'bird', 'chicken', 'house', 'building', 'city', "running", "flying"]
ref_word = 'animal'

word_vectors = [model.get_vector(word, norm=True) for word in words]
ref_vector = model.get_vector(ref_word, norm=True)

#plot each vector as a barcode image foollowed by the corresponding word
result = plt.subplots(len(words), 2, figsize=(6, 2*len(words)))

ax : list[plt.Axes] = result[1]

for i, word in enumerate(words):
    v = word_vectors[i]
    ax[i,0].imshow(v.reshape(1, -1), aspect='auto', vmin=-1.0, vmax=1.0, cmap='RdBu')
    ax[i,0].set_yticks([])
    ax[i,0].set_xticks([])
    ax[i,0].set_title(word, fontsize=12)

    sim = word_vectors[i]* ref_vector
    sim_v = np.sum(sim)
    ax[i,1].imshow(sim.reshape(1, -1), aspect='auto', vmin=-0.1, vmax=0.1, cmap='RdBu')
    ax[i,1].set_yticks([])
    ax[i,1].set_xticks([])
    ax[i,1].set_title(f'{word} x {ref_word} = {sim_v:.2f}', fontsize=12)

plt.tight_layout()
plt.show()
