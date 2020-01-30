# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 06:36:18 2020

@author: 81802
"""

import urllib.request
from bs4 import BeautifulSoup
import csv
from pychord import ChordProgression


def chord_url():
    url='https://ja.chordwiki.org/ranking.html'
    url_2="https://ja.chordwiki.org/wiki.cgi?c=edit&t="
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    lists = soup.find_all("table",{"class": "ranking"})[0].findAll('tr')
    sets = [[int(i.find('td').text[:-1]), i.findAll('td')[4].contents[0].text,url_2+(i.findAll('td')[4].contents[0].attrs['href'])[6:]] for i in lists]
    sets_2=[]
    for i in sets:
        sets_2.append(i[2])
    return sets_2

def chord_getter():
    c=chord_url()
    chords=[]
    chord_2=[]
    for i in c:
        html=urllib.request.urlopen(str(i))
        soup = BeautifulSoup(html, "html.parser")
        lists=soup.find_all("textarea",{"name": "chord"})[0]
        for j in lists:
            a=str(j).split('[')
            for k in a:
                if '}' not in k and 'N.C.' not in k:
                   b=k.split(']')
                   if ">" not in b[0]:
                      if "/" in b[0]:
                         c=str(b[0]).split("/")
                         if "(" in c[0]:
                             e=str(c[0]).split("(")
                             if e[0] != '':
                                chords.append(e[0])
                         else:chords.append(c[0])
                      elif "(" in b[0]:
                           e=str(b[0]).split("(")
                           if e[0] != '':
                              chords.append(e[0])                          
                      else:chords.append(b[0])
                        
        chord_2.append(chords) 
        chords=[]         
                   
    return chord_2

cp = ChordProgression(chord_getter()[0])

with open('test2.csv', 'w') as csv_file:   
     writer = csv.writer(csv_file, lineterminator='\n')  # 改行コード（\n）を指定しておく
     writer.writerows(str(cp))

