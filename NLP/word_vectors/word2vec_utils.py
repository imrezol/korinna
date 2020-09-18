from os import path
from gensim.test.utils import datapath
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

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