import gensim
import logging
import os
import numpy as np
import math

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

#here are a few helper methods to work with the word - vectors
#compute the dot product of two vectors
def dot(a, b):
    #we could also use numpy for this operation whicih would be faster for large vectors
    #sum = np.dot(a,b)
    #but for pedagogical purposes we will use the manual loop here

    sum = 0.0
    for i in range(len(a)):
        sum += a[i]*b[i]

    return sum

#compute the norm of a vector as : sqrt(a.a)
def norm(a):
    return math.sqrt(dot(a,a))

#normalize a vector by dividing all its components by its norm
def normalize(a):
    na = norm(a)
    return a / na

#compute the cosine similarity between two vectors as : a.b/(norm(a)*norm(b))
def similarity(a, b):
    norm_a = norm(a)
    norm_b = norm(b)
    return dot(a,b)/(norm_a * norm_b)

#A. vectorize a single word
word = 'whale'
print(f'A Vectorizing a single word:{word}')
#check if word exists
if word in model:
    #get the raw word vector as a numpy array (list of numbers)
    word_vec = model.get_vector(word)
    print(word_vec)

    #get the normalized word vector, We will use this one for most operations as vector norm is not important for similarity queries
    norm_word_vec = model.get_vector(word, True)
    print(norm_word_vec)

print('\n\n') #add a few blank lines for better readability


#B. vectorize 3 words and check their similarity
print(f'B. Comparing the similarity between 3 words')
cat = model.get_vector('cat', True)
dog = model.get_vector('dog', True)
mouse = model.get_vector('mouse', True)

print(f'similarity between cat and dog is {similarity(cat, dog)}')
print(f'similarity between cat and mouse is {similarity(cat, mouse)}')
print(f'similarity between dog and mouse is {similarity(dog, mouse)}')

print('\n\n') #add a few blank lines for better readability

#C. find the most similar words to a given word
print(f'C. Finding the most similar words to a given word')
word = 'whale'
words = model.most_similar(positive = word, topn=10)
print(f'the 10 most similar words to {word} are:')
print(words)

print('\n\n') #add a few blank lines for better readability

#D. find the most similar words to a given word, but exclude another word
print(f'D. Finding the most similar words to a given word, but exclude another word')
positive_term = 'whale'
negative_term = 'water'
words = model.most_similar(positive = positive_term, negative=negative_term, topn=10)
print(f'the 10 most similar words to {positive_term} opposite {negative_term} are:')
print(words)

print('\n\n') #add a few blank lines for better readability

#E. compute an analogy : Find the word that is to A what C is to B
#this can be done by vector arithmetic moving A along the  (B-C) direction
#X = A - B + C
A = 'good'
B = 'bad'
C = 'worse'

print(f'E. Computing an analogy: Find the word that is to {A} what {C} is to {B}')

a = model.get_vector(A, True)
b = model.get_vector(B, True)
c = model.get_vector(C, True)
vec = a-b+c
vec = normalize(vec)
results = model.similar_by_vector(vec, topn=10)
print(f'the 10 most similar words to {A}-{B}+{C} are:')
print(results)

print('\n\n') #add a few blank lines for better readability

#F. Sort words by similarity to a given word
print(f'F. Sorting words by similarity to a given word')
words = ['art' , 'science', 'religion', 'politics', 'economics', 'building', 'urban', 'dog', 'cat', 'ant', 'bee', 'landscape', 'site', 'material', 'modern', 'contemporary', 'engineering', 'good', 'bad', 'ugly', 'beautiful', 'design', 'city', 'country', 'authoritarian', 'democratic']
ref_word = 'architecture'

#get the vector of the reference word
ref_word_vec = model.get_vector(ref_word, True)

#compute the similarity of all words to the reference word
#we are going to build a list where each word is represented by a tuple (word, similarity)
sims = []
for w in words:
    vec = model.get_vector(w, True)
    sim = similarity(ref_word_vec, vec)
    pair = (w, sim)
    sims.append(pair)

#sort the list by similarity
sims.sort(key=lambda x: x[1], reverse=True)

print(f'the words sorted by similarity to {ref_word} are:')
for w, sim in sims:
    print(f'{w} : {sim}')
