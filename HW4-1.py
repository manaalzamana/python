import urllib.request
from urllib.error import URLError
import re
import pickle
import sys

Tuple=()
List=[]
def url(url, domain, Tuple, List):
    global crawler
    if(len(crawler)>10):
        return
    if(url in crawler and crawler[url] == 1):
        return
    else:
        crawler[url] = 1

    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")
            regexp_title = re.compile('<title>(?P<title>.*)</title>')
            regexp_url = re.compile("http://"+domain+"[/\w+]*")
            result = regexp_title.search(content_string, re.IGNORECASE)
            
            if result:
                title = result.group("title")
                title=title[26:]
                title_list=title.split()
                for title_word in title_list:
                    Tuple=(url, title)
                    List.append(Tuple)



            for (URL) in re.findall(regexp_url, content_string):
                    if(URL not in crawler or crawler[URL] != 1):
                        crawler[urls] = 0
                        url(URL, domain, Tuple, List)

                        
    except URLError as Error:
        print("error")

    x = open("raw_data.txt","bw")
    pickle.dump(List,x)
    x.close

crawler = {}
seed = "http://www.newhaven.edu/"
crawler[seed]=0
url(seed,"www.newhaven.edu" , Tuple, List)
