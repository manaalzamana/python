@@ -0,0 +1,50 @@
import os
import fnmatch
import pickle
import quotes
from quotes import data_list
from datetime import datetime
def search():
    query = input("Search:")
    query = query.split()
    query = set(query)
    query = list(query)
    dt1 = datetime.now() 
    dt2 = datetime.now()


    if "and" in (query):
        query.remove("and")
        if "or" in (query):
            query.remove("or")
        print (query)
     

        for quote in (data_list):
            if query[0] in quote and query[0] in quote:
                print(quote)
        print("Execution time:", dt2.microsecond - dt1.microsecond)
     

    elif "or" in (query) and "and" not  in (query):
        query.remove("or")
        print (query)
     

        for quote in (data_list):
            for (value) in (query):
                found_at = quote.find(value)
                if( found_at > 0):
                    print(quote)
        print("Execution time:", dt2.microsecond - dt1.microsecond)
     
    else:
        print (query)

        for quote in (data_list):
            if query[0] in quote and query[0] in quote:
                print(quote)
        print("Execution time:", dt2.microsecond - dt1.microsecond)
     

search()
