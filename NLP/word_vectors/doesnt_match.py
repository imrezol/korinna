from word2vec_utils import load_model

model = load_model("glove.6B.50d")

print(model.doesnt_match("breakfast cereal dinner lunch".split()))
