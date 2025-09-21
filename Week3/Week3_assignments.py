# Week 3 Assignments, 9/20/25
# Quantitative Aesthetics, Fall 2025
# David Selles

# imports
import gensim
import os
import numpy as np
import math

import matplotlib.pyplot as plt #for plotting if needed

# Importing only the necessary modules for vectors
from gensim.models import KeyedVectors
import gensim.downloader

# To handle SSL certificate issues (if any) during model download. Especially on MacOS.
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

model_name = "glove-wiki-gigaword-50"
model: KeyedVectors = gensim.downloader.load(model_name)
print(f"Model '{model_name}' loaded successfully.")

# test functionality
# result = model.most_similar('whale', topn=10) #test similarity of whale to other words
# print(f"Top 10 words similar to 'whale': {result}")

# Assignment 1: Semantic Axis
# Axis 1: Beaultiful - Ugly
# Starting word: architecture : architecture + (beautiful - ugly)
origin = model.get_vector('architecture', norm=True) # normalized vector for 'architecture'
beautiful_vec = model.get_vector('beautiful', norm=True) # normalized vector for 'beautiful'
ugly_vec = model.get_vector('ugly', norm=True) # normalized vector for 'ugly'
axis1_vec = beautiful_vec - ugly_vec
result1_vec = origin + axis1_vec

closest_words1 = model.similar_by_vector(result1_vec, topn=10)
# printing the list of closest words with their similarity scores
# print(f'Closest words to "architecture" on the "beautiful - ugly" axis: {closest_words1}')

# # display the results in a more readable format
# print('Closest words to "architecture" on the "beautiful - ugly" axis:')
# for word, score in closest_words1:
#     print(f'Word: {word}, Similarity Score: {score}')

# add some space for readability
print('\n')

print("Assignment 1: Semantic Axis \n")
print("Axis 1: Beautiful -> Ugly, Starting word: Architecture")
print("Axis: Beautiful -> Ugly : architecture + (beautiful - ugly)")
# make the number of spaces (indentation) of each word to be related to its similarity value.
for word, score in closest_words1:
    # print(' ' * int((1 - score) * 50) + word + ":(" + str(round(score,2)) + ")")  # Adjust the multiplier for more or less indentation as needed
    # same thing but using f-string formatting
    print(f"{' ' * int((1 - score) * 50)}{word}:({score:.2f})")

print('')
print("Axis 1 reverse: Ugly -> Beautiful : architecture + (ugly - beautiful)")
axis1_reverse_vec = ugly_vec - beautiful_vec
result1_reverse_vec = origin + axis1_reverse_vec
closest_words1_reverse = model.similar_by_vector(result1_reverse_vec, topn=10)
for word, score in closest_words1_reverse:
    print(f"{' ' * int((1 - score) * 50)}{word}:({score:.2f})")

# Axis 2: Miniature - Giant
# Starting word: architecture : architecture + (beautiful - ugly)
print('')
print("Axis 2: Miniature -> Giant, Starting word: Cat")
print("Axis: Miniature -> Giant : cat + (miniature - giant)")
miniature_vec = model.get_vector('miniature', norm=True) # normalized vector for 'miniature'
giant_vec = model.get_vector('giant', norm=True) # normalized vector for 'giant'
cat_vec = model.get_vector('cat', norm=True) # normalized vector for 'cat'

axis2_vec = miniature_vec - giant_vec
result2_vec = cat_vec + axis2_vec

closest_words2 = model.similar_by_vector(result2_vec, topn=10)
for word, score in closest_words2:
    print(f"{' ' * int((1 - score) * 50)}{word}:({score:.2f})")

# Axis 2 reverse: Giant -> Miniature
print('')
print("Axis 2 reverse: Giant -> Miniature : cat + (giant - miniature)")
axis2_reverse_vec = giant_vec - miniature_vec
result2_reverse_vec = cat_vec + axis2_reverse_vec
closest_words2_reverse = model.similar_by_vector(result2_reverse_vec, topn=10)
for word, score in closest_words2_reverse:
    print(f"{' ' * int((1 - score) * 50)}{word}:({score:.2f})")

# Axis 3: Best - Worst
# Starting word: emotion : emotion + (best - worst)
print('')
print("Axis 3: Best -> Worst, Starting word: Emotion")
print("Axis: Best -> Worst : emotion + (best - worst)")
best_vec = model.get_vector('best', norm=True) # normalized vector for 'best'
worst_vec = model.get_vector('worst', norm=True) # normalized vector for 'worst'
emotion_vec = model.get_vector('emotion', norm=True) # normalized vector for 'emotion'
axis3_vec = best_vec - worst_vec
result3_vec = emotion_vec + axis3_vec
closest_words3 = model.similar_by_vector(result3_vec, topn=10)
for word, score in closest_words3:
    print(f"{' ' * int((1 - score) * 50)}{word}:({score:.2f})")

# Axis 3 reverse: Worst -> Best
print('')
print("Axis 3 reverse: Worst -> Best : emotion + (worst - best)")
axis3_reverse_vec = worst_vec - best_vec
result3_reverse_vec = emotion_vec + axis3_reverse_vec
closest_words3_reverse = model.similar_by_vector(result3_reverse_vec, topn=10)
for word, score in closest_words3_reverse:
    print(f"{' ' * int((1 - score) * 50)}{word}:({score:.2f})")

print('\n\n') #add a few blank lines for better readability

# Assignment 2: Bi-axial Semantics
print("Assignment 2: Bi-axial Semantics \n")
# Axis 1: Beautiful - Ugly
# Axis 2: Best - Worst
# Starting word: emotion

print("Starting word: Emotion")
print("Axis 1: Beautiful -> Ugly")
print("Axis 2: Best -> Worst")
print("Combinations of both axes applied to the starting word:\n")

origin = model.get_vector('emotion', norm=True) # normalized vector for 'emotion'
beautiful_vec = model.get_vector('beautiful', norm=True) # normalized vector for 'beautiful'
ugly_vec = model.get_vector('ugly', norm=True) # normalized vector for 'ugly'
best_vec = model.get_vector('best', norm=True) # normalized vector for 'best'
worst_vec = model.get_vector('worst', norm=True) # normalized vector for 'worst'

axis1_vec = beautiful_vec - ugly_vec
axis2_vec = best_vec - worst_vec
axis1_reverse_vec = ugly_vec - beautiful_vec
axis2_reverse_vec = worst_vec - best_vec

# Eight Combinations
combinations = {
    "Beautiful": axis1_vec,
    "Beautiful + Best": axis1_vec + axis2_vec,
    "Best": axis2_vec,
    "Ugly + Best": axis1_reverse_vec + axis2_vec,
    "Ugly": axis1_reverse_vec,
    "Ugly + Worst": axis1_reverse_vec + axis2_reverse_vec,
    "Worst": axis2_reverse_vec,
    "Beautiful + Worst": axis1_vec + axis2_reverse_vec
}

for combo_name, combo_vec in combinations.items():
    result_vec = origin + combo_vec
    closest_words = model.similar_by_vector(result_vec, topn=10)
    print(f'Combination: {combo_name}')
    for word, score in closest_words:
        print(f"{' ' * int((1 - score) * 50)}{word}:({score:.2f})")
    print('')  # Add a blank line between combinations

