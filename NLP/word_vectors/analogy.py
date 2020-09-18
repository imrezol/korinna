from word2vec_utils import load_model

def analogy(x1, x2, y1):
    result = model.most_similar(positive=[y1, x2], negative=[x1])
    y2 = result[0][0]
    print(x2, "-", x1, "+", y1, "=", y2)
    return y2

model = load_model("glove.6B.50d")

analogy('man', 'king', 'woman')