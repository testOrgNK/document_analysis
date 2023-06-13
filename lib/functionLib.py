import re
from pandas import DataFrame
from nltk.corpus import stopwords
import string
from collections import Counter

stop = stopwords.words("english")


def clean_text(df: DataFrame = None, column: str = "") -> DataFrame:
    df[column] = df[column].apply(lambda x: re.sub("[^A-Za-z]+", " ", x))
    df[column] = df[column].apply(lambda x: x.lower())
    df[column] = df[column].apply(lambda x: x.strip())
    return df


def counter_wrd(text: str = "") -> int:
    cnt = Counter()
    for i in text.values:
        for word in i.split():
            cnt[word] += 1
    return cnt


def remove_stop(text: str = "") -> str:
    final_text = []
    for i in text.split():
        if i.strip().lower() not in stop:
            final_text.append(i.strip())
    return " ".join(final_text)
