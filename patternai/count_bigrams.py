import sys
from collections import Counter
import pprint

from nltk.util import bigrams
from nltk.tokenize import RegexpTokenizer

#Set up a tokenizer which only captures lowercase letters and spaces
#This requires that input has been preprocessed to lowercase all letters
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
        #This step is needed to collapse runs of space characters into one
        text = ' '.join(text.split())
        spans = TOKENIZER.span_tokenize(text)
        tokens = (text[begin : end] for (begin, end) in spans)
        for bigram in bigrams(tokens):
            #Increment the count for the bigram. Automatically handles any
            #bigram not seen before. The join expression turns 2 separate 
            #single-character strings into one 2-character string
            frequencies[''.join(bigram)] += 1
        #Read the next chunk of text, and set all letters to lowercase
        text = input_fp.read(buffer_size).lower()

    return


if __name__ == '__main__':
    #Initialize the mapping
    frequencies = Counter()
    #Pull the input data from the console
    count_bigrams(sys.stdin, frequencies)
    #Uncomment the following line to display all the resulting frequencies
    #in readable format
    #pprint.pprint(frequencies)
    #Print just the 20 most common bigrams and their frequencies
    #in readable format
    pprint.pprint(frequencies.most_common(20))
