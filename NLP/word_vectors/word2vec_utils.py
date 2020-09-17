from os import path
from gensim.test.utils import datapath
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
#plt.style.use('ggplot')

def get_word2vec_file(filename):
    word2vec_glove_file = path.expanduser("~/PycharmProjects/korinna/large_files/" + filename + ".word2vec.txt")
    if path.exists(word2vec_glove_file):
        return word2vec_glove_file
    glove_file = datapath(path.expanduser("~/PycharmProjects/korinna/large_files/" + filename + ".txt"))
    print("Converting " +filename+ " glove file to word2vec format")
    glove2word2vec(glove_file, word2vec_glove_file)
    print(filename + " word2vec ready")
    return word2vec_glove_file

def load_model(name):
    print("Loading model")
    model = KeyedVectors.load_word2vec_format(get_word2vec_file(name))
    print("Model loaded")
    return model

def display_pca_scatterplot(model, words=None, sample=0):
    if words == None:
        if sample > 0:
            words = np.random.choice(list(model.vocab.keys()), sample)
        else:
            words = [word for word in model.vocab]

    word_vectors = np.array([model[w] for w in words])

    twodim = PCA().fit_transform(word_vectors)[:, :2]

    plt.figure(figsize=(6, 6))
    plt.scatter(twodim[:, 0], twodim[:, 1], edgecolors='k', c='r')
    for word, (x, y) in zip(words, twodim):
        plt.text(x + 0.05, y + 0.05, word)
    plt.show()