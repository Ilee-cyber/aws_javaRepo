#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:13:33 2020

@author: Gary
"""

import re    #we need this module to define regex
import os    
import os.path
import string
import nltk
from nltk.tokenize import MWETokenizer  #import tokenizer
nltk.download('stopwords')  #download the list of stopwords, if you have not already done so
from nltk.corpus import stopwords  #import the list of stopwords
from nltk.stem.snowball import SnowballStemmer  #import stemmer module
import pandas as pd

# define the following the function 
def cmp(a, b):
    return (a > b) - (a < b)

def negation_handling (text):
    negatereg1=re.compile(r'n’t \S*') #look for patterns
    negatereg2=re.compile(r'no \S*')
    negatereg3=re.compile(r'not \S*')
    
    negate_list1=negatereg1.findall(docu)
    negate_list2=negatereg2.findall(docu)
    negate_list3=negatereg3.findall(docu)
    negate_list = negate_list1 + negate_list2 + negate_list3

    text1 = re.sub(negatereg1,'', text) #delete these words
    text2 = re.sub(negatereg2,'', text1) 
    text3 = re.sub(negatereg3,'', text2) 
    
    return text3, negate_list #the news article after removing all the neglating combinations and a list

def clean_tokenize (text):
    # remove numbers
    text_nonum = re.sub(r'\d+', '', text)
    text_nonum = text_nonum.replace('”', '')
    text_nonum = text_nonum.replace('“', '')
    text_nonum = text_nonum.replace('—', ' ')
    # remove punctuations and convert characters to lower case
    text_nopunct = "".join([char.lower() for char in text_nonum if char not in string.punctuation]) 
    # substitute multiple whitespace with single whitespace. Also, removes leading and trailing whitespaces
    text_cleaned = re.sub('\s+', ' ', text_nopunct).strip()
    text_output = tokenizer.tokenize(text_cleaned.split())
    text_stopwords = []
    for word in text_output:
        if word not in stopwords.words('english'):  #filter the stop words
            text_stopwords.append(word) 
    text_stemmed = ([stemmer.stem(w) for w in text_stopwords])
    return text_stemmed

# record the number of each type of article 

pe = 0
ind = 0
op = 0
total = 0

# step1: read in the text information
curDir = os.getcwd()   #check: where is the working directory
os.chdir('/Users/jason/Desktop/Project Resources')  #check: change to the current working directory
for parent, dirnames, filenames in os.walk(curDir):
    for filename in filenames: # go on and on until all the news we collected are read
        basename, extname = os.path.splitext(filename) # read in txt file only
        if cmp(extname, '.txt') == 0:
            total += 1 # record the number of news read
            file_in = open(filename, encoding='utf-8', errors='ignore')
            docu = file_in.read()
            file_in.close()
            
            # step2: negation handling
            stemmer = SnowballStemmer('english')
            docu_negate, nlist = negation_handling(docu) # call the function
            nlist_stemmed = ([stemmer.stem(w) for w in nlist])
            
            # step3: remove punctuations, remove stopwords, stem and tokenize
            tokenizer = MWETokenizer([('new', 'york'), ('san', 'francisco')])
            stemmer = SnowballStemmer('english')
            docu_tokens = clean_tokenize(docu_negate)
            
            # step4: read in the Excel Spreadsheet 
            df1 = pd.read_excel('Computational Finance Spreadsheet Data Dictonary.xlsx',sheet_name = 'Pessimistic')
            pessimistic_temp = df1['WORD'].tolist()
            pessimistic = [item.lower() for item in pessimistic_temp]
            pessimistic_stemmed = ([stemmer.stem(w) for w in pessimistic])
            pessimistic_negate = []
            for word in pessimistic_stemmed:
                pessimistic_negate.append('n’t '+ word)
                pessimistic_negate.append('no '+ word)
                pessimistic_negate.append('not '+ word)
            
            df2 = pd.read_excel('Computational Finance Spreadsheet Data Dictonary.xlsx',sheet_name = 'Indifference')
            indifference_temp = df2['WORD'].tolist()
            indifference = [item.lower() for item in indifference_temp]
            indifference_stemmed = ([stemmer.stem(w) for w in indifference])
            
            df3 = pd.read_excel('Computational Finance Spreadsheet Data Dictonary.xlsx',sheet_name = 'Optimistic')
            optimistic_temp = df3['WORD'].tolist()
            optimistic = [item.lower() for item in optimistic_temp]
            optimistic_stemmed = ([stemmer.stem(w) for w in optimistic])
            optimistic_negate = []
            for word in optimistic_stemmed:
                optimistic_negate.append('n’t '+ word)
                optimistic_negate.append('no '+ word)
                optimistic_negate.append('not '+ word)
            
            pessimistic_final = pessimistic_stemmed + optimistic_negate
            optimistic_final = optimistic_stemmed + pessimistic_negate
            
            # step5: get the sentiment of each article
            docufinal = docu_tokens + nlist_stemmed
            
            doculen = len(docufinal)
            docu_pessimistic = ([w for w in docufinal if w in pessimistic_final]) 
            docu_indifference = ([w for w in docufinal if w in indifference_stemmed])
            docu_optimistic = ([w for w in docufinal if w in optimistic_final])
            
            pessimistic_sentiment = len(docu_pessimistic)/doculen 
            indifference_sentiment = len(docu_indifference)/doculen 
            optimistic_sentiment = len(docu_optimistic)/doculen
            
            list1 = [pessimistic_sentiment, indifference_sentiment, optimistic_sentiment] # store the value in a list for later use
            
            article_sentiment = max(list1) # determine the sentiment of each article

            # update the number of each type of article
            if article_sentiment == pessimistic_sentiment:
                pe += 1
                print('The outlook of article ' + basename + ' is pessimistic.' )
            elif article_sentiment == indifference_sentiment:
                ind += 1
                print('The outlook of article ' + basename + ' is indifference.' )
            elif article_sentiment == optimistic_sentiment:
                op += 1
                print('The outlook of article ' + basename + ' is optimistic.' )


# determine the market perception - future perspective tone
list2 = [pe, ind, op]
market_perception = max(list2)

def get_perception(number1, number2, number3, number4):
    if number1 == number2:
        return 'pessimistic'
    elif number1 == number3:
        return 'indifference'
    elif number1 == number4:
        return 'optimistic'

tone = get_perception(market_perception, pe, ind, op)

print('\n')
print('The number of articles we read is', total, '\n'
      'The number of pessimistic articles is', pe, '\n'
      'The number of indifference articles is', ind, '\n'
      'The number of optimistic articles is', op, '\n')
print('We believe the market is ' + tone + ' about the oil industry.')




            
                        