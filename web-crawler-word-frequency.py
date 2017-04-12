# Word Frequency counter with web crawler
import requests
from bs4 import BeautifulSoup
import operator

# Words list in the dictionary
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

# Remove symbols from Dictionary
def clean_up_words(word_list):
    clean_words_dic=[]
    for word in word_list:
        symbols="!@#$%^&*()_\"'.]["
        for j in range(0,len(symbols)):
            word = word.replace(symbols[j],"")
        if len(word)>0:
            clean_words_dic.append(word)
    create_counter_words_dic(clean_words_dic)

# count word from dictionary
def create_counter_words_dic(clean_words_dic):
    counter_words_dic={}
    for word in clean_words_dic:
        if word in counter_words_dic:
            counter_words_dic[word]+=1
        else:
            counter_words_dic[word]=1
    for key,value in sorted(counter_words_dic.items(),key=operator.itemgetter(1)):
        print(key,value)

start("http://techblog.ankitaoza.com/page/2/")
