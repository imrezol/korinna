from word2vec_utils import load_model, display_pca_scatterplot

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