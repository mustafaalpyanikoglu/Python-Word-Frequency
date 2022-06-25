from importlib.resources import contents
import requests
import operator
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


def createDictionary(allWords):
    wordCount = {}
    for word in allWords:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount


URL = "https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"

r = requests.get(URL)
allWords = []

soup = BeautifulSoup(r.content, "html.parser")

# kelimler ve sembollü halleri
for wordGroups in soup.find_all("p"):
    contents = wordGroups.text
    # lower() ile büyük küçük harf ayrımını kaldırdık // split() ile boşluklara göre kelimeleri ayıracak
    words = contents.lower().split()
    print(words)
    for word in words:
        allWords.append(word)
        print(word)

allWords = clearSymbols(allWords)
# for word in allWords:
#     print(word)
print("\n-------------------------------\n")
wordCount = createDictionary(allWords)
# 0 dersek kelimeleri sıralar // 1 dersek en çok geçenleri sıralar
for key, value in sorted(wordCount.items(), key=operator.itemgetter(1)):
    print(key, value)
