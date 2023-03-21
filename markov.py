"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text = ''
    # for file in file_path:
    text_file = open(file_path)
    text = text + text_file.read()
    text_file.close()

    return text

def make_chains(text_string,n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}

    # your code goes here
    words = text_string.split() # Split the text into a list of words

    # Loop over each pair of adjacent words in the list
    for i in range(len(words) -n):

        # Get the current word pair and the next word
        key_pair = tuple(words[i:i + n])
        value = words[i + n]

        # If the current word pair is not
        # already a key in the chains dictionary, add it
        if key_pair not in chains:
            chains[key_pair] = []

        # Add the next word to the
        # list of values for the current word pair key
        chains[key_pair].append(value)

    # Return the dictionary of chains
    return chains


def make_text(chains):
    """Return text from chains."""

    punctuation = ([",","?","!"])
    words = []
    # Get a random key to start with
    key = choice(list(chains.keys()))
    keys = list(chains.keys())

    # your code goes here
    # Loop until the next word is None (i.e. the end of the chain)
    while not key[0][0].isupper():
        key = choice(keys)
    words = list(key)
    word = choice(list(chains[key]))

    while word is not None:
        key = key[1:] + (word,)
        words.append(word)
        if word[-1] in punctuation:
             break
        word = choice(chains[key])
    
    return ' '.join(words)


# input_path = 'green-eggs.txt'

# Open the file and turn it into one long string

input_path = sys.argv[1]
input_text = open_and_read_file(input_path)

# Get a Markov chain
#chains = make_chains(input_path)

chains= make_chains(input_text, 2)
print(chains)
# Produce random text
random_text = make_text(chains)

print(random_text)