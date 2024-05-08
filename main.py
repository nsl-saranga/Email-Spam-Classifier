import nltk
import pandas as pd
nltk.download()

rawData = open('SMSSpamCollection.tsv').read() # python sees this as a very long string.
# print(rawData[0:500])

parsedData = rawData.replace('\t', '\n').split('\n')
# print(parsedData[0:9])

labelList = parsedData[0::2]
textList = parsedData[1::2]

# print(labelList)
# print(textList)

fullCorpus = pd.DataFrame(
    {
        "label": labelList[:-1],
        "text": textList
    }
)

fullCorpus.head()


