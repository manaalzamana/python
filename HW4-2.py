import os
import pickle
import quotes
import shelve



def indexer():
    Dictionry = {}
    pickles = open ("\Users\GhasanAlyamani\raw_data.pickle","br")
    n = pickle.load(r)
    shelve = shelve.open("data_list")
    for n, quote in enumerate(quotes.data_list):
        words = quote.split()
        for word in words:
            if(word not in Dictionry.keys()):
                Dictionry[word]={n}
            else:
                Dictionry[word]= Dictionry[word]|{n}
    for key, value in Dictionry.items():
        shelve[key]=(value)
    pickles.close()
    shelve.close()

indexer()
