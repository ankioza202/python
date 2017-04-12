# Word Frequency counter with web crawler
import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list=[]
    response=requests.get(url).text
    soup=BeautifulSoup(response,"html.parser")
    post_title=soup.findAll('h2',{'class':'entry-title'})
    for n in post_title:
        a=n.find('a')
        words=n.text
        word_split=words.lower().split()
        for each_word in word_split:
            word_list.append(each_word)
    clean_up_words(word_list)

def clean_up_words(word_list):
    clean_dic=[]
    for word in word_list:
        symbols="!@#$%^&*()_\"'.]["
        for j in range(0,len(symbols)):
            word = word.replace(symbols[j],"")
        if len(word)>0:
            print(word)
            clean_dic.append(word)

start("http://techblog.ankitaoza.com/page/2/")
