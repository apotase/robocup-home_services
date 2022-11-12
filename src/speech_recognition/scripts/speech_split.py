import nltk

a1 = 'My name is Tracy.'
a2 = 'My name is'
a3 = "I'm Joey."
a4 = 'I am Jack'
a5 = 'eh my name is eh'
a6 = 'my name is eh, Amy.'
a7 = 'Mike'
a8 = "Jessie."
SENTENCES = [a1, a2, a3, a4, a5, a6, a7, a8]

def extract_info(sentence):
    '''
    extract useful information from a full sentence
    !! can only extract one word, needs to be fixed!!
    '''
    sentences = sentence.strip('.')
    text = nltk.word_tokenize(sentences)
    #词性标注
    tagged = nltk.pos_tag(text)
    print(tagged)
    if len(tagged) == 1:
        return tagged[0][0]
    for index, word in enumerate(tagged):
        if 'VB' in word[1] and index + 1 < len(tagged):
            if tagged[index+1][1] == 'NNP' or tagged[index+1][1] == "JJ":
                return tagged[index+1][0]
    return ''

# if __name__ == "__main__":
#     for index, sentence in enumerate(SENTENCES):
#         print(index+1, extract_info(sentence))