from ast import parse
from site import venv
import sys, glob, math
from urllib import request

from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from nltk.tokenize import sent_tokenize

# GET LENGTH OF GIVEN INPUT
def inputLen(input):
    number_of_sentences = sent_tokenize(input)

    return len(number_of_sentences)

# SUMMARISE THE GIVEN PARSER TO GIVEN LENGTH
def summarise(parser, len):
    stemmer = Stemmer("english")

    summarizer = LsaSummarizer(stemmer)
    summarizer.null_words = get_stop_words("english")

    summary = summarizer(parser.document, len)
    final = ""

    for sentence in summary:
        final = final + str(sentence) + "\n\n"

    return final

# SUMMARISE TEXT (GIVEN STRING)
def summariseText(originalString):
    from sumy.parsers.plaintext import PlaintextParser

    x = originalString.splitlines() # Split given string into array (Paragraphs)
    
    arrayLength = len(x) # Get length of array ax
    
    # Set variables
    i = 0
    finalArray = []

    # Loop array till i = length of x
    while i < arrayLength:   
        parser = PlaintextParser.from_string(x[i], Tokenizer("english")) # Set parser with array address = loop interation

        outputLen = math.ceil(inputLen(x[i])/4) # Get length of 1/4 array address round up 

        finalArray.append(str(summarise(parser, outputLen))) # Add summarised array address to finalarray (1/4 length original)

        i += 1 # Increase i

    final = ''.join(finalArray) # Collapse array to string
    return final # return string

def summariseURL(passedURL):
    from sumy.parsers.html import HtmlParser
    
    parser = HtmlParser.from_url(passedURL, Tokenizer("english")) # Set parser with given url

    # Add url text to string urlText
    uf = request.urlopen(passedURL)
    urlText = uf.read()

    # Get length 1/4 urlText set outputLen
    outputLen = math.ceil(inputLen(str(urlText))/4)

    # Summarise url text to output len set Final
    final = summarise(parser, outputLen)

    return final # Return final

def summariseFile(passedAddress):
    from sumy.parsers.plaintext import PlaintextParser

    # Original file parser (Replaced with plaintext for text tiling
    # parser = PlaintextParser.from_file(passedAddress, Tokenizer("english")) 


    # Get URL text set to fileText
    with open(passedAddress) as f:
        fileText = f.readlines()
    
    arrayLength = len(fileText) # Get length of x
    
    # Set variables
    i = 0
    finalArray = [] 

    # Loop array till i = length of x
    while i < arrayLength:   
        parser = PlaintextParser.from_string(fileText[i], Tokenizer("english")) # Set parser with array address = loop interation

        outputLen = math.ceil(inputLen(fileText[i])/4) # Get length of 1/4 array address round up 

        finalArray.append(str(summarise(parser, outputLen))) # Add summarised array address to finalarray (1/4 length original)

        i += 1 # Increase i

    final = ''.join(finalArray) # Collapse array to string

    return fileText, final # Return final and file text