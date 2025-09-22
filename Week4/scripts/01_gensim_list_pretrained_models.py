#before starting install gensim writing in a terminal :  
#pip install gensim 
#or on MacOS
#pip3 install gensim

#this script list all available pretrained models in gensim
#pre-trained models are dictionary-like objects that can be queried for word embeddings using a word as a key
#the models store an N dimensional vector for each word in the vocabulary
#N is the number of dimensions of the word embedding and is usually somewhere between 50 and 300
#the higher the number of dimensions, the more accurate the model is, but also the more computationally expensive
#the models can be used to compute the similarity between words

import gensim
import gensim.downloader

#need this to avoid SSL certificate error when downloading models from gensim api. Especially on MacOS
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


#list all available models
print('List of available models:')
info = gensim.downloader.info()
for model_name, model_data in sorted(info['models'].items()):
    print(
        '%s (%d records):\n\t%s' % (
            model_name,
            model_data.get('num_records', -1),
            model_data['description'][:256] + '...\n',
        )
    )

