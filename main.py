from importlib.resources import contents
import requests
from bs4 import BeautifulSoup


def clearSymbols(allWords):
    wordsWithoutSymbols = []
    symbols = "!@$^*()_+{}\"<>?,./:'[]-="+chr(775)
    for word in allWords:
        for symbol in symbols:
            if symbol in word:
                word = word.replace(symbol, "")
        if(len(word) > 0):
            wordsWithoutSymbols.append(word)
    return wordsWithoutSymbols


URL = "https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"

r = requests.get(URL)
allWords = []

soup = BeautifulSoup(r.content, "html.parser")

for wordGroups in soup.find_all("p"):
    contents = wordGroups.text
    # lower() ile büyük küçük harf ayrımını kaldırdık // split() ile boşluklara göre kelimeleri ayıracak
    words = contents.lower().split()
    print(words)
    for word in words:
        allWords.append(word)
        print(word)

allWords = clearSymbols(allWords)
for word in allWords:
    print(word)
