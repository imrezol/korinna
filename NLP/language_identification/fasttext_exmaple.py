# https://fasttext.cc/docs/en/language-identification.html
# wget -O lid.176.bin https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin

# third party libraries, dependencies
import fasttext
import bs4
import urllib.request

PRETRAINED_MODEL_PATH = './lid.176.bin'
model = fasttext.load_model(PRETRAINED_MODEL_PATH)
# scope
k =3
threshold = 0.1

# dictionary
languages =	{
  "__label__en": "English",
  "__label__hu": "Hungarian",
}


def get_language_name(langId):
    language = languages.get(langId) # scope, dictionary
    if language == None: # Null value
        return langId
    else:
        return language

def print_predictions(title, predictions):
    print(title+" preditions:")
    # array
    languages = predictions[0]  #scope
    scores = predictions[1]
    for i in range(len(languages)):
        # variable types, conversion
        print(str(i + 1)+".", get_language_name(languages[i]), ' language probability:',scores[i])
    print()


predictions = model.predict("je mange de la nourriture", k, threshold)
print_predictions("pure France",predictions)

predictions = model.predict("Which baking dish is best to bake a banana bread ?", k, threshold)
print_predictions("pure English",predictions)

link = "https://stackoverflow.com/questions/30951657/download-only-the-text-from-a-webpage-content-in-python"
webpage=str(urllib.request.urlopen(link).read())
soup = bs4.BeautifulSoup(webpage,"html.parser")
#print(soup.get_text())
predictions = model.predict(soup.get_text(), k, threshold)
print_predictions("stackoverflow", predictions)

link = "https://444.hu/"
webpage=str(urllib.request.urlopen(link).read())
soup = bs4.BeautifulSoup(webpage,"html.parser")
predictions = model.predict(soup.get_text(), k, threshold)
print_predictions("444.hu", predictions)

predictions = model.predict("je mange de la nourriture. Which baking dish is best to bake a banana bread ?", k, threshold)
print_predictions("Mixed English and France", predictions)
