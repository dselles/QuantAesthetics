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
    'Week4/scripts/ruskin_7_lamps.kv',
    'Week4/scripts/vitruvius_10_books.kv',
    'Week4/scripts/PrideAndPrejudice.kv'
]

#we pick on of those models 
model_name = model_files[0]

#and we load the selected model
model: KeyedVectors = KeyedVectors.load(model_name, mmap='r')


#or if we wanted to use a pretrained model...
# model_name = 'glove-wiki-gigaword-50'
# model: KeyedVectors = gensim.downloader.load(model_name)

#print out some information about the model we loaded
print(f"Loaded model: {model_name} : word count : {len(model.index_to_key)}")

#these are the 4 cardinal points that will form the X and Y axes for our plot
#each word vector will be projected onto these axes
east_w = 'happy'
west_w = 'sad'
north_w = 'hate'
south_w = 'love'

#we also store these 4 cardinal words in a list for easy access
cardinal_w = [east_w, west_w, north_w, south_w]

#these are the words we are going to plot. Notice we join the list of cardinal words with some other words
words_to_plot = ["edgar", "alice", "money", "son"] + cardinal_w

#we get the normalized vectors for the 4 cardinal words
east_v = model.get_vector(east_w, norm=True)
west_v = model.get_vector(west_w, norm=True)
north_v = model.get_vector(north_w, norm=True)
south_v = model.get_vector(south_w, norm=True)


#form the X and Y axes as the difference between the two opposite cardinal vectors
axis_x = east_v - west_v
axis_y = north_v - south_v

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
word_color = (1.0, 0.3, 1.0)
cardinal_color = (0.0, 1.0, 1.0)
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

#now iterate over the words to plot and place them in the plot according to their similarity to the two axes
for word in words_to_plot:
    #get the normalized vector for the word
    v = model.get_vector(word, norm=True)
    
    #compute the similarity to the two axes
    x = sim(v, axis_x)
    y = sim(v, axis_y)

    #plot a dot and the word
    ax.plot(x, y, 'o', markersize=40, alpha=0.1, color=dot_color)

    #set the color depending on if the word is a cardinal word or a regular word
    color = word_color if word in cardinal_w else cardinal_color    

    #draw the word text
    ax.text(x, y, word, fontsize=12, ha='center', va='center', color=color)

plt.show()
#____________________________END PLOT