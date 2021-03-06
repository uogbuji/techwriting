import sys
import json
from nltk.probability import FreqDist

from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer

#Set up a tokenizer which only captures lowercase letters and spaces
#This requires that input has been preprocessed to lowercase all letters
TOKENIZER = RegexpTokenizer("[a-z ]")


def count_ngrams(input_fp, frequencies, order, buffer_size=1024):
    '''Read the text content of a file and keep a running count of how often
    each bigram (sequence of two) characters appears.

    Arguments:
        input_fp -- file pointer with input text
        frequencies -- mapping from each bigram to its counted frequency
        buffer_size -- incremental quantity of text to be read at a time,
            in bytes (1024 if not otherwise specified)
        order -- The N in each N-gram (i.e. number of items)

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
        for bigram in ngrams(tokens, order):
            #Increment the count for the bigram. Automatically handles any
            #bigram not seen before. The join expression turns 2 separate 
            #single-character strings into one 2-character string
            if '  ' not in ''.join(bigram):
                frequencies[''.join(bigram)] += 1
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
