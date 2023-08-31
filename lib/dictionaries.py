import string

def word_frequency(sentence):
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    words = sentence.lower().split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency
