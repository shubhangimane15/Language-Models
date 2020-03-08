import json
# if you are using python 3, you should 
import urllib.request
import urllib.parse 
from langdetect import detect

url = "http://ec2-18-191-67-129.us-east-2.compute.amazonaws.com:8983/solr/"
core = "Lang"
url_remain = "/select?q="
url_tail = "&fl=id%2Cscore&wt=json&indent=true&rows=20"

#outf = open("output_BM14505.txt", 'a+')

i = 1
with open("test_queries.txt","r", encoding="utf-8") as f:
    for line in f:
        splitted = line.split(" ",1)
        qid = splitted[0]
        query = splitted[1]
        query = query.replace(":","")
        query = "("+query+")"
        outfn = str(i) + '.txt'
        outf = open(outfn, 'a+') 
        finalUrl = url+core+url_remain+"text_en%3A"+urllib.parse.quote(query)+"+"+"text_de%3A"+urllib.parse.quote(query)+"+"+"text_ru%3A"+urllib.parse.quote(query)+url_tail
        print(finalUrl)
        data = urllib.request.urlopen(finalUrl)
        docs = json.load(data)['response']['docs']
        # the ranking should start from 1 and increase
        core1 = 'LM'
        rank = 1
        for doc in docs:
            outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + core1 + '\n')
            rank += 1
        outf.close()
        i += 1

