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

word_vectors = [model.get_vector(word, norm=True) for word in words]

#create the correlation matrix
corr_matrix = np.zeros((len(words), len(words)))

for i, vec1 in enumerate(word_vectors):
    for j, vec2 in enumerate(word_vectors):
        corr_matrix[i, j] = np.dot(vec1, vec2)
        #corr_matrix[i, j] = np.sum(vec1 * vec2)

#plot the correlation matrix as a heatmap
plt.imshow(corr_matrix, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.xticks(ticks=np.arange(len(words)), labels=words, rotation=90)
plt.yticks(ticks=np.arange(len(words)), labels=words)
plt.title('Word Vectors Correlation Matrix')
plt.tight_layout()
plt.show()
