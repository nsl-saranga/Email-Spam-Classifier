import pandas as pd
import string
import re
import nltk

df = pd.read_csv('SMSSpamCollection.tsv', sep='\t', header=None)
df.columns = ["Labels", "Texts"]
# print(df)
# print(len(df[df['Labels'] == "ham"]))
# print(len(df[df['Labels'] == "spam"]))
# print(df["Labels"].isnull().sum())
# print(df["Labels"].isnull().sum())
print(string.punctuation)


def remove_punctuation(text):
    removed_punctuation_text = ""
    for char in text:
        if char not in string.punctuation:
            removed_punctuation_text += char
    return removed_punctuation_text


df["punctuation_removed_text"] = df["Texts"].apply(remove_punctuation)


def tolkenize(text):
    tolkens = re.split('\W+',text)
    return tolkens


df["lowercased_text"] = df["punctuation_removed_text"].str.lower()

df["tolkenized _text"] = df["lowercased_text"].apply(tolkenize)


nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')


def remove_stopwords(tolkenized_text):
    removed_stopwords_list = []
    for word in tolkenized_text:
        if word not in stopwords:
            removed_stopwords_list.append(word)
    return removed_stopwords_list


df["stopword_removed_text"] = df["tolkenized _text"].apply(remove_stopwords)

print(df.head())
