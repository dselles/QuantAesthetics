import numpy as np
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
import gensim.downloader

#in this example we will load a pretrained word embedding model and plot some words in a 2D space
#the position of each word in the 2D space will be determined by its similarity to two axes formed by 4 cardinal words X = east-west and Y = north-south
#this is equivalent to defining a two dimensional plane in the high dimensional word embedding space and projecting the word vectors onto that plane

#these are the files of precomputed word embeddings in our working directory
model_files = [
    'Week4/scripts/dance_of_death.kv',
    'Week4/scripts/moby_dick.kv',
    'Week4/scripts/vitruvius_10_books.kv',
    'Week4/scripts/ruskin_7_lamps.kv',    
    'Week4/scripts/PrideAndPrejudice.kv',
    'Week4/scripts/the_origin_of_species.kv'
]

#we pick on of those models 
model_name_a = model_files[4]
model_name_b = model_files[5]

#and we load the selected model
model_a: KeyedVectors = KeyedVectors.load(model_name_a, mmap='r')
model_b: KeyedVectors = KeyedVectors.load(model_name_b, mmap='r')


#or if we want to use a pretrained model...
# model_name = 'glove-wiki-gigaword-50'
# model: KeyedVectors = gensim.downloader.load(model_name)

#print out some information about the model we loaded
print(f"Loaded model A: {model_name_a} : word count : {len(model_a.index_to_key)}")
print(f"Loaded model B: {model_name_b} : word count : {len(model_b.index_to_key)}")

#these are the 4 cardinal points that will form the X and Y axes for our plot
#each word vector will be projected onto these axes
east_w = 'night'
west_w = 'day'
north_w = 'few'
south_w = 'most'

#we also store these 4 cardinal words in a list for easy access
cardinal_w = [east_w, west_w, north_w, south_w]

#these are the words we are going to plot. Notice we join the list of cardinal words with some other words
words_to_plot = [] + cardinal_w

#EDIT FOR ASSIGNMENT

centeral_w = 'music'
words_to_plot.append(centeral_w)
#find the 10 closest words to the centeral word in both models and add them to the words_to_plot list if they are not already in it
closest_words1 = model_a.similar_by_vector(centeral_w, topn=10)
closest_words2 = model_b.similar_by_vector(centeral_w, topn=10)
for word, score in closest_words1:
    if word not in words_to_plot:
        if word in model_a and word in model_b:
            words_to_plot.append(word)
for word, score in closest_words2:
    if word not in words_to_plot:
        if word in model_a and word in model_b:
            words_to_plot.append(word)


#we get the normalized vectors for the 4 cardinal words
east_v_a = model_a.get_vector(east_w, norm=True)
west_v_a = model_a.get_vector(west_w, norm=True)
north_v_a = model_a.get_vector(north_w, norm=True)
south_v_a = model_a.get_vector(south_w, norm=True)

east_v_b = model_b.get_vector(east_w, norm=True)
west_v_b = model_b.get_vector(west_w, norm=True)
north_v_b = model_b.get_vector(north_w, norm=True)
south_v_b = model_b.get_vector(south_w, norm=True)

#form the X and Y axes as the difference between the two opposite cardinal vectors
axis_x_a = east_v_a - west_v_a
axis_y_a = north_v_a - south_v_a

axis_x_b = east_v_b - west_v_b
axis_y_b = north_v_b - south_v_b

#define two functions to compute the similarity between two vectors
#one using a manual loop and one using numpy dot product
def sim_manual(a, b):
    dot = 0.0
    for i in range(len(a)):
        dot += a[i] * b[i]
    return dot

def sim(a, b):
    return np.dot(a, b)
#

#____________________________PLOT
#create a plot where each word is placed according to its similarity to the east-west and north-south axes

#we sstore the colors in variables so we can change them easily
#that's a good practice when you want to tweak and customize code parameters
#as we have all the customization variables in one place
word_color_a = (1.0, 0.5, 1.0)
cardinal_color_a = (0.8, 0.3, 0.8)

word_color_b = (0.5, 1.0, 1.0)
cardinal_color_b = (0.3, 0.8, 0.8)

dot_color = (1.0, 1.0, 1.0)
bg_color = (0.1, 0.2, 0.25)
frame_color = (0.5, 0.5, 0.5)
frame_text_color = (0.8, 0.8, 0.8)
axes_color = (0.0, 0.0, 0.0)

#create the plot (returns a figure and an axis object) The axis is the area where the data is plotted and the figure is the whole window. A figure can contain multiple axes 
fig, ax = plt.subplots(figsize=(10, 8))

#set the font globally for the plot
plt.rcParams['font.family'] = 'monospace'

#set the various colors
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

ax.spines['left'].set_color(frame_color)
ax.spines['bottom'].set_color(frame_color)
ax.spines['right'].set_color(frame_color)
ax.spines['top'].set_color(frame_color)

ax.xaxis.label.set_color(frame_text_color)
ax.yaxis.label.set_color(frame_text_color)
ax.title.set_color(frame_text_color)
ax.tick_params(axis='both', colors=frame_text_color)

#set the extents of the plot otherwise the axes will automatically adjust to the data but in our case we know that similarities are always between -1 and 1
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-1.0, 1.0)

#show a faint grid (opacity 0.1)
ax.grid(True, alpha=0.1)

#set the labels and title
ax.set_xlabel(f'Similarity to "{west_w}" -> "{east_w}" axis')
ax.set_ylabel(f'Similarity to "{south_w}" -> "{north_w}" axis')
ax.set_title('Word Bi-axial Semantic Map')

#draw the two axres lines crossing at the origin
ax.axhline(0, color=axes_color, linewidth=0.5)
ax.axvline(0, color=axes_color, linewidth=0.5)

#add a legend explaining the two models
ax.text(0.95, 0.95, f'Model A: {model_name_a}',
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes,
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.5),
        color=word_color_a)

#add a legend explaining the two models
ax.text(0.95, 0.85, f'Model B: {model_name_b}',
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes,
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.5),
        color=word_color_b)

#now iterate over the words to plot and place them in the plot according to their similarity to the two axes
for word in words_to_plot:
    #get the normalized vector for the word
    v_a = model_a.get_vector(word, norm=True)
    v_b = model_b.get_vector(word, norm=True)
    
    #compute the similarity to the two axes
    x_a = sim(v_a, axis_x_a)
    y_a = sim(v_a, axis_y_a)

    x_b = sim(v_b, axis_x_b)
    y_b = sim(v_b, axis_y_b)

    #plot a dot and the word
    ax.plot(x_a, y_a, 'o', markersize=40, alpha=0.1, color=dot_color)
    ax.plot(x_b, y_b, 'o', markersize=40, alpha=0.1, color=dot_color)

    #set the color depending on if the word is a cardinal word or a regular word
    color_a = cardinal_color_a if word in cardinal_w else word_color_a
    color_b = cardinal_color_b if word in cardinal_w else word_color_b

    #draw the word text
    ax.text(x_a, y_a, word, fontsize=12, ha='center', va='center', color=color_a)
    ax.text(x_b, y_b, word, fontsize=12, ha='center', va='center', color=color_b)

plt.show()
#____________________________END PLOT