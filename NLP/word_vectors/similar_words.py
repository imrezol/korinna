from word2vec_utils import load_model

model = load_model("glove.6B.50d")

similar_words = model.most_similar('obama')
print(*similar_words, sep = "\n")
print()

similar_words = model.most_similar('apple')
print(*similar_words, sep = "\n")
print()
