import sys
import json
import string
import random

POPULAR_NGRAM_COUNT = 10000

#Population is all the possible items that can be generated
population = ' ' + string.ascii_lowercase

def preprocess_frequencies(frequencies, order):
    '''Compile simple mapping from N-grams to frequencies into data structures to help compute
    the probability of state transitions to complete an N-gram

    Arguments:
        frequencies -- mapping from N-gram to frequency recorded in the training text
        order -- The N in each N-gram (i.e. number of items)

    Returns:
        sequencer -- Set of mappings from each N-1 sequence to the freqency of possible
            items completing it
        popular_ngrams -- list of most common N-grams
    '''
    sequencer = {}
    ngrams_sorted_by_freq = [
        k for k in sorted(frequencies, key=frequencies.get, reverse=True)
    ]
    popular_ngrams = ngrams_sorted_by_freq[:POPULAR_NGRAM_COUNT]
    for ngram in frequencies:
        #Separate the N-1 lead of each N-gram from its item completions
        freq = frequencies[ngram]
        lead = ngram[:-1]
        final = ngram[-1]
        sequencer.setdefault(lead, {})
        sequencer[lead][final] = freq
    return sequencer, popular_ngrams


def generate_letters(sequencer, popular_ngrams, length, order):
    '''Generate text based on probabilities derived from statistics for initializing
    and continuing sequences of letters

    Arguments:
        sequencer -- mapping from each leading sequence to frequencies of the next letter
        popular_ngrams -- list of the highest frequency N-Grams
        length -- approximate number of characters to generate before ending the program
        order -- The N in each N-gram (i.e. number of items)

    Returns:
        nothing
    '''
    #The lead is the initial part of the N-Gram to be completed, of length N-1
    #containing the last N-1 items produced
    lead = ''
    #Keep track of how many items have been generated
    generated_count = 0
    while generated_count < length:
        #This condition will be true until the initial lead N-gram is constructed
        #It will also be true if we get to a dead end where there are no stats
        #For the next item from the current lead
        if lead not in sequencer:
            #Pick an N-gram at random from the most popular
            reset = random.choice(popular_ngrams)
            #Drop the final item so that lead is N-1
            lead = reset[:-1]
            for item in lead:
                print(item, end='', flush=True)
            generated_count += len(lead)
        else:
            freq = sequencer[lead]
            weights = [ freq.get(c, 0) for c in population ]
            chosen = random.choices(population, weights=weights)[0]
            print(chosen, end='', flush=True)
            #Clip the first item from the lead and tack on the new item
            lead = lead[1:] + chosen
            generated_count += 1

    return


if __name__ == '__main__':
    #File with N-gram frequencies is the first argument
    raw_freq_fp = open(sys.argv[1])
    length = int(sys.argv[2])
    raw_freqs = json.load(raw_freq_fp)
    
    #Figure out the N-gram order. Just pull the first N-gram and check its length
    order = len(next(iter(raw_freqs)))
    sequencer, popular_ngrams = preprocess_frequencies(raw_freqs, order)
    generate_letters(sequencer, popular_ngrams, length, order)

