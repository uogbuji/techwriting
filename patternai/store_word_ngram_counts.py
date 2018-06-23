import sys
import json
from nltk.probability import FreqDist

from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer

#Set up a tokenizer which only captures words
#Requires that input has been preprocessed to lowercase all letters
TOKENIZER = RegexpTokenizer("[a-z]+")


def count_ngrams(input_fp, frequencies, order, buffer_size=1024):
    '''Read the text content of a file and keep a running count of how often
    each bigram (sequence of two) characters appears.

    Arguments:
        input_fp -- file pointer with input text
        frequencies -- mapping from each bigram to its counted frequency
        order -- The N in each N-gram (i.e. number of items)
        buffer_size -- incremental quantity of text to be read at a time,
            in bytes (1024 if not otherwise specified)

    Returns:
        nothing
    '''
    #Read the first chunk of text, and set all letters to lowercase
    text = input_fp.read(buffer_size).lower()
    #Loop over the file while there is text to read
    while text:
        #This step is needed to collapse runs of space characters into one
        text = ' '.join(text.split())
        spans = TOKENIZER.span_tokenize(text)
        tokens = (text[begin : end] for (begin, end) in spans)
        for ngram in ngrams(tokens, order):
            #Join ngrams into a single space separated string
            ngram_text = ' '.join(ngram)
            #Extra layer to make sure no multiple runs of spaces sneak through
            ngram_text = ' '.join(ngram_text.split())
            frequencies[ngram_text] += 1
        #Read the next chunk of text, and set all letters to lowercase
        text = input_fp.read(buffer_size).lower()

    return


if __name__ == '__main__':
    #Initialize the mapping
    frequencies = FreqDist()
    #The order of the ngrams is the first command line argument
    ngram_order = int(sys.argv[1])
    #Pull the input data from the console
    count_ngrams(sys.stdin, frequencies, ngram_order)
    outputfp = open(sys.argv[2], 'w')
    json.dump(dict(frequencies), outputfp)
    print('Stored frequencies of {} encountered N-grams.'.format(len(frequencies)))
