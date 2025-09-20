import gensim
import logging
import os
import numpy as np
import math

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


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


words = ['cat', 'dog', 'animal', 'bird', 'chicken', 'house', 'building', 'city']

word_vectors = np.array([model.get_vector(word) for word in words])


pca = PCA(n_components=2)
result = pca.fit_transform(word_vectors)
#get the words corresponding to the PCA vectors

axis_x_vec = pca.components_[0]
axis_y_vec = pca.components_[1]

axis_x_words = model.similar_by_vector(axis_x_vec, topn=5)
axis_y_words = model.similar_by_vector(axis_y_vec, topn=5)

print(f'X axis words: {axis_x_words}')
print(f'Y axis words: {axis_y_words}')

# create a scatter plot of the projection with centered white labels on gray background
fig, ax = plt.subplots()
ax.set_facecolor((0.7, 0.7, 0.7))
ax.scatter(result[:, 0], result[:, 1], color='black', zorder=2)
for i, word in enumerate(words):
    ax.text(result[i, 0], result[i, 1], word,
            ha='center', va='bottom',
            color='white', fontsize=16,
            zorder=3)
plt.tight_layout()
plt.show()
