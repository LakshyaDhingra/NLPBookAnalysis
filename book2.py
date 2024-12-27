import re
# Below statements need to be done once before output
# nltk.download("stopwords")
# nltk.download("vader_lexicon")
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer


with open("miracle_in_the_andes.txt", "r") as file:
    book = file.read()


pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())

d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1


d_list = [(value, key) for (key, value) in d.items()]
d_list = sorted(d_list, reverse=True)

english_stopwords = stopwords.words("english")

filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))

print(filtered_words[:10])

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(book)
if scores["pos"] > scores["neg"]:
    print("Positive text")
else:
    print("Negative text")

pattern2 = re.compile("Chapter [0-9]+")
chapters = re.split(pattern2, book)
chapters = chapters[1:]

for index, chapter in enumerate(chapters):
    scores2 = analyzer.polarity_scores(chapter)
    if scores2["pos"] > scores2["neg"]:
        print(f"Chapter {index + 1} is a Positive chapter")
    else:
        print(f"Chapter {index + 1} is a Negative chapter")
