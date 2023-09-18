import string

def word_frequency(sentence):
    
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    
    
    words = sentence.split()
    
    
    word_freq = {}
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

