import sys
import pprint
from nltk.util import bigrams
from nltk.tokenize import RegexpTokenizer

TOKENIZER = RegexpTokenizer("[a-z ]")


def count_bigrams(input_fp, frequencies, buffer_size=1024):
    '''Read the text content of a file and keep a running count of how often
    each bigram (sequence of two) characters appears.

    Arguments:
        input_fp -- file pointer with input text
        frequencies -- mapping from each bigram to its counted frequency
        buffer_size -- incremental quantity of text to be read at a time,
            in bytes (1024 if not otherwise specified)

    Returns:
        nothing
    '''
    #Read the first chunk of text, and set all letters to lowercase
    text = input_fp.read(buffer_size).lower()
    #Loop over the file while there is text to read
    while text:
        spans = TOKENIZER.span_tokenize(text)
        tokens = (text[begin : end] for (begin, end) in spans)
        for bigram in bigrams(tokens):
            #Accommodate the bigram if seen for the first time
            frequencies.setdefault(bigram, 0)
            #Increment the count for the bigram
            frequencies[bigram] += 1
        #Read the next chunk of text, and set all letters to lowercase
        text = input_fp.read(buffer_size).lower()

    return


if __name__ == '__main__':
    #Initialize the mapping
    frequencies = {}
    #Pull the input data from the console
    count_bigrams(sys.stdin, frequencies)
    #Display the resulting frequencies in readable format
    pprint.pprint(frequencies)
