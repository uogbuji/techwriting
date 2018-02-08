import sys
import pprint
import string

WHITELIST_CHARACTERS = string.ascii_lowercase + ' '

def count_chars(input_fp, frequencies, whitelist=WHITELIST_CHARACTERS,
                    buffer_size=1024):
    '''Read the text content of a file and keep a running count of how often
    each character appears.

    Arguments:
        input_fp -- file pointer with input text
        frequencies -- mapping from each character to its counted frequency
        whitelist -- string containing all characters to be included in the stats
            defaults to all lowercase letters and space
        buffer_size -- incremental quantity of text to be read at a time,
            in bytes (1024 if not otherwise specified)

    Returns:
        nothing
    '''
    #Read the first chunk of text, and set all letters to lowercase
    text = input_fp.read(buffer_size).lower()
    #Loop over the file while there is text to read
    while text:
        for c in text:
            if c in WHITELIST_CHARACTERS:
                #Accommodate the character if seen for the first time
                frequencies.setdefault(c, 0)
                #Increment the count for the present character
                frequencies[c] += 1
        #Read the next chunk of text, and set all letters to lowercase
        text = input_fp.read(buffer_size).lower()

    return


if __name__ == '__main__':
    #Initialize the mapping
    frequencies = {}
    #Pull the input data from the console
    count_chars(sys.stdin, frequencies)
    #Display the resulting frequencies in readable format
    pprint.pprint(frequencies)
