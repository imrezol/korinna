# https://fasttext.cc/docs/en/language-identification.html
# wget -O lid.176.bin https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin

# third party libraries, dependencies

import fasttext
import bs4
import requests
import certifi
import ssl

# download the model file (it was taught from wikipedia with 176 languages):
# wget -O ~/PycharmProjects/korinna/large_files/lid.176.bin2 https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
PRETRAINED_MODEL_PATH = '../../large_files/lid.176.bin'
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
    probabilities = predictions[1]
    for i in range(len(languages)):
        # variable types, conversion
        print(str(i + 1)+".", get_language_name(languages[i]), ' language probability:',probabilities[i])
    print()

def get_text_from_web(link):
    # r = requests.get(link, verify=certifi.where())
    r = requests.get(link)
    encoding = r.encoding if 'charset' in r.headers.get('content-type', '').lower() else None
    soup = bs4.BeautifulSoup(r.content, from_encoding=encoding, features="lxml")
    return soup.get_text().replace("\n","")

predictions = model.predict("je mange de la nourriture", k, threshold)
print_predictions("pure France",predictions)

predictions = model.predict("Which baking dish is best to bake a banana bread ?", k, threshold)
print_predictions("pure English",predictions)

link = "https://stackoverflow.com/questions/30951657/download-only-the-text-from-a-webpage-content-in-python"
predictions = model.predict(get_text_from_web(link), k, threshold)
print_predictions("stackoverflow", predictions)

link = "https://444.hu/2020/10/08/kina-nyeresre-all-a-koronavirus-ellen/"
predictions = model.predict(get_text_from_web(link), k, threshold)
print_predictions("444.hu", predictions)

predictions = model.predict("je mange de la nourriture. Which baking dish is best to bake a banana bread ?", k, threshold)
print_predictions("Mixed English and France", predictions)
