"""
#Here are all the installs and imports you will need for your word cloud script and uploader widget

pip install wordcloud
python -m pip install -U pip
python -m pip install -U matplotlib

#from IPython.display import display
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = 344
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)


# FINAL project

"""
problem:
  create a "word cloud" from the given text
  a word cloud counts the number of times a word appears in text

  input:
    the given text

    output:
      remove words that are short and/or not interesting like 'the', 'of, 'a', 'if', etc
      counts of each word in the text

"""

"""
file_contents = "The Cat in the Hat By Dr. Seuss " \
       "The sun did not shine. " \
       "It was too wet to play. " \
       "So we sat in the house " \
       "All that cold, cold, wet day. " \
       "I sat there with Sally. " \
       "We sat there, we two. " \
       "And I said, 'How I wish " \
       "we had something to do! " \
       "Too wet to go out " \
       "And too cold to play ball. " \
       "So we sat in the house. " \
       "We did nothing at all. " \
       "So all we could do was to " \
       "Sit! " \
       "Sit! " \
       "Sit! " \
       "Sit! "
"""


file_contents = ""


def calculate_frequencies(file_contents, exclude_words):
    # uninteresting words
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i",
        "me", "my","we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her",
                           "hers", "its","they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are",
                           "was", "were", "be",
                           "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with",
                           "from", "here", "when",
                           "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can",
                           "will", "just"]

    if type(exclude_words) is set:
        uninteresting_words = exclude_words

    file_contents = open("cat in the hat.txt").read()

    word = ""
    # use dictionary to count words; word is key and count is value
    frequencies = {}

    # filter punctuation, character-by-character, using the isalpha() method.
    for letter in file_contents:
        if letter.isalpha():
            word += letter.lower()
        else:
            # add word to dict and count
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1
            word = ""

    # remove uninteresting words
    for x in uninteresting_words:
        frequencies.pop(x, None)

    print (frequencies)

    # wordcloud
    wordcloud = WordCloud(font_path=r'C:\Windows\Fonts\Verdana.ttf',
                          stopwords=STOPWORDS,
                          background_color='white',
                          max_words=500,
                          width=1200,
                          height=1000,
                          color_func=random_color_func).generate(file_contents)

    wordcloud.generate_from_frequencies(frequencies)
    # save the file too   cloud.to_file("myfile.jpg")
    wordcloud.to_file("cat_in_the_hat.jpg")

    return wordcloud.to_array()


# Display your wordcloud image  {'a','if','to'}
myimage = calculate_frequencies(file_contents, None)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
