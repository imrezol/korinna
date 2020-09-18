from word2vec_utils import load_model
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
plt.style.use('ggplot')

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

model = load_model("glove.6B.50d")

# display_pca_scatterplot(model,
#                         ['coffee', 'tea', 'beer', 'wine', 'brandy', 'rum', 'champagne', 'water',
#                          'spaghetti', 'borscht', 'hamburger', 'pizza', 'falafel', 'sushi', 'meatballs',
#                          'dog', 'horse', 'cat', 'monkey', 'parrot', 'koala', 'lizard',
#                          'frog', 'toad', 'monkey', 'ape', 'kangaroo', 'wombat', 'wolf',
#                          'france', 'germany', 'hungary', 'luxembourg', 'australia', 'fiji', 'china',
#                          'homework', 'assignment', 'problem', 'exam', 'test', 'class',
#                          'school', 'college', 'university', 'institute'])

#display_pca_scatterplot(model, sample=300)

display_pca_scatterplot(model,
                        ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december',
                         'obama', 'reagan', 'clinton', 'bush',
                         'london', 'paris', 'berlin',
                         'apple', 'banana', 'orange', 'grapefruit', 'pineapple', 'grapes', 'cherry', 'pear', 'plum',
                         'could', 'would', 'might', 'can'])